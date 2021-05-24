# -*- coding: utf-8; mode: python -*-

import sys
import os.path
import time
import logging
import subprocess
import functools
import itertools
import math
from subprocess import Popen, PIPE

# print 0
import requests
from requests_futures.sessions import FuturesSession

import hgapi
import gitapi
# import OpenSSL

logging.getLogger("requests").setLevel(logging.WARNING)
logger = logging.getLogger('bucket')

import exceptions as exc
from commodity.pattern import MetaBunch
from commodity.thread_ import SimpleThreadPool

import lurl


bitbucket_org = 'bitbucket.org'
BB_API1 = 'https://api.bitbucket.org/1.0/'
BB_API2 = 'https://api.bitbucket.org/2.0/'

PROTO_SSH = 'ssh'
PROTO_HTTPS = 'https'


def git_cmd(path, *args):
    """Run a git command in path and return the result. Throws on error."""
    if not path:
        path = '.'

    proc = Popen(["git"] + list(args), stdout=PIPE, stderr=PIPE, cwd=path)
    out, err = [x.decode("utf-8") for x in proc.communicate()]

    if proc.returncode:
        cmd = "git " + " ".join(args)
        raise gitapi.gitapi.GitException(
            "Error running %s:\n\tErr: %s\n\tOut: %s\n\tExit: %s"
            % (cmd,err,out,proc.returncode), exit_code=proc.returncode)

    return out, err


def hg_cmd(path, *args):
    """Run a git command in path and return the result. Throws on error."""
    if not path:
        path = '.'

    proc = Popen(["hg"] + list(args), stdout=PIPE, stderr=PIPE, cwd=path)
    out, err = [x.decode("utf-8") for x in proc.communicate()]

    if proc.returncode:
        cmd = "hg " + " ".join(args)
        raise hgapi.hgapi.HgException(
            "Error running %s:\n\tErr: %s\n\tOut: %s\n\tExit: %s"
            % (cmd, err, out, proc.returncode), exit_code=proc.returncode)

    return out, err


def bb_api1_uri(path):
    uri = BB_API1 + path
    return uri


def bb_api2_uri(path):
    uri = BB_API2 + path
    return uri


def reply2json(reply, ok=None):
    ok = ok or 200

    if reply.status_code != ok:
        logger.info(reply.content)
        raise exc.RemoteException.from_reply(reply)

    if not reply.content:
        return None

    try:
        return reply.json()
    except ValueError as e:
        logger.critical("{}: {}".format(e, reply.text))
        raise


class Account(object):
    def __init__(self, username=None, password=None):
        self.username = username or "anonymous"
        self.password = password

    # @classmethod
    # def from_args(cls, *args):
    #     assert len(args) == 2
    #     return Account(str.join(':', args))

    def is_anonymous(self):
        return self.username == "anonymous"

    def __str__(self):
        pwd = '*' * len(self.password) if self.password else None
        return '"{}:{}"'.format(self.username, pwd)


class Session(object):
    def __init__(self, account=None, logger=None, verbose=False):
        self.account = account
        self.timeout = 10
        self._http_session = None
        self.logger = logger or logging.getLogger('bucket')

        self.verbose = verbose

    def auth(self):
        if self.account is None or self.account.is_anonymous():
            return None

        return (self.account.username, self.account.password)

    @property
    def http_session(self):
        if self._http_session is not None:
            return self._http_session

        self._http_session = FuturesSession(max_workers=10)
        self._http_session.auth = self.auth()
        self._http_session.timeout = self.timeout
        return self._http_session

    def request(self, method, path, data=None, ok=None):
        self.logger.debug("request '%s' '%s' '%s'", method, path, data)
        while 1:
            url = path if path.startswith('http') else bb_api2_uri(path)
            try:
                future = self.http_session.request(method, url, data=data)
                reply = future.result()
                retval = reply2json(reply, ok=ok)
                break

            except exc.ServiceUnavailable:
                time.sleep(1)

            except requests.exceptions.ConnectionError, e:
                self.logger.error(e)
                sys.exit(1)

        return retval

    def async_request(self, method, path, data=None, ok=None):
        def to_json(sess, reply):
            try:
                reply.data = reply.json()
            except ValueError as e:
                self.logger.critical("{}: {}".format(e, reply.text))
                raise

        self.logger.debug("async request %s %s %s", method, path, data)
        url = path if path.startswith('http') else bb_api2_uri(path)
        return self.http_session.request(method, url, data=data, background_callback=to_json)

    def async_get(self, path, **kargs):
        return self.async_request('get', path, **kargs)

    def http_get(self, path, **kargs):
        return self.request('get', path, **kargs)

    def http_put(self, path, **kargs):
        return self.request('put', path, **kargs)

    def http_post(self, path, **kargs):
        for key, val in kargs['data'].copy().items():
            if val is None:
                del kargs['data'][key]

        return self.request('post', path, **kargs)

    def http_delete(self, path, **kargs):
        return self.request('delete', path, **kargs)

    def __repr__(self):
        return "<Session '%s'>" % self.account


class SyncStatus:
    UPDATE = "update"
    CLONED = "cloned"
    PULLED = "pulled"


class Repo(object):
    def __init__(self, manager, full_name=None, dirname=None):
        assert self.__class__ is not Repo
        assert isinstance(manager, RepoManager)
        self.manager = manager
        self.full_name = full_name
        self.dirname = dirname
        self._data = None
        self._api_repo = None
        self._uris = None
        self._custom_args = []

    @classmethod
    def from_remote(cls, manager, full_name):
        try:
            data = MetaBunch(manager.get_repo_info(full_name))
            repo_cls = {'hg': HgRepo, 'git': GitRepo}[data.scm]
            retval = repo_cls(manager, data['full_name'])

        except exc.RemoteException as e:
            if e.reason.upper() == "NOT_FOUND":
                raise exc.NoSuchRepo()
            raise

        retval._data = data
        return retval

    @classmethod
    def from_remote_async(cls, manager, future):
        try:
            data = MetaBunch(future.result().data)
            repo_cls = {'hg': HgRepo, 'git': GitRepo}[data.scm]
            retval = repo_cls(manager, data['full_name'])
        except exc.RemoteException as e:
            if e.reason == "NOT_FOUND":
                raise exc.NoSuchRepo()
            raise

        retval._data = data
        return retval

    @classmethod
    def from_dir(cls, manager, dirname=None):
        dirname = dirname or os.path.join(os.getcwd())

        try:
            return HgRepo.from_dir(manager, dirname)
        except hgapi.HgException as hg_e:
            pass

        try:
            return GitRepo.from_dir(manager, dirname)
        except gitapi.gitapi.GitException as git_e:
            pass

        logger.debug("LocalRepo('%s'):\n%s", dirname, hg_e)
        logger.debug("LocalRepo('%s'):\n%s", dirname, git_e)
        raise exc.NoSuchRepo(dirname)

    @property
    def data(self):
        if self._data is None:
            self._data = MetaBunch(self.manager.get_repo_info(self.full_name))

        return self._data

    @property
    def slug(self):
        return self.full_name.split('/')[1]

    @property
    def basename(self):
        return os.path.split(self.dirname)[1]

    @property
    def api_repo(self):
        if self._api_repo is None:
            self._build_api_repo()

        return self._api_repo

    def as_dict(self):
        retval = {}
        for k in 'name full_name is_private scm size access'.split():
            retval[k] = self[k]

        return retval

    def __getitem__(self, key):
        if key == 'webpage':
            return self.webpage

        if key == 'access':
            return self.access

        return self._data[key]

    def is_private(self):
        return self._data.is_private

    @property
    def access(self):
        return 'private' if self.is_private() else 'public'

    @property
    def webpage(self):
        return self._data.links.html.href

    @property
    def scm(self):
        if self._api_repo is not None:
            scms = {hgapi.Repo: 'hg', gitapi.Repo: 'git'}
            return scms[self._api_repo.__class__]

        return self._data.scm

    def _get_origin_by_rest(self, proto):
        return self._get_origin_sid(proto)

    def _get_origin_by_cmd(self, proto=PROTO_HTTPS):
        assert proto in [PROTO_HTTPS, PROTO_SSH]

        try:
            self.origin = self._do_get_origin_by_cmd()
            # print("======", self.origin)
            url = lurl.parse(self.origin)
            url = lurl.change_login(url)

            if url.scheme == proto:
                return url.geturl()

            return lurl.change_proto(url, proto).geturl()
        except KeyError:
            return None

    @classmethod
    def _get_full_name(cls, origin):
        url = lurl.parse(origin)
        if url.hostname != bitbucket_org:
            return None

        return cls._sanitize_full_name(url.path)

    @classmethod
    def _sanitize_full_name(cls, full_name):
        return full_name.strip('/')

    def _apply_pwd(self, origin):
        url = lurl.parse(origin)
        if url.scheme == PROTO_HTTPS:
            username = self.manager.session.account.username
            password = self.manager.session.account.password
            return lurl.change_login(url, username, password).geturl()

        return origin

    def clone(self, proto, destdir):
        try:
            if self.dirname is None:
                self.dirname = destdir

            return self._do_clone(proto, destdir)
        except (hgapi.hgapi.HgException, gitapi.gitapi.GitException, UnicodeDecodeError) as e:
            raise exc.CloneError(e)

    def commited(self):
        return

    def pushed(self):
        return

    def __cmp__(self, other):
        assert isinstance(other, Repo)
        return cmp(self.full_name, other.full_name)

    def __eq__(self, other):
        return self.scm == other.scm and self.full_name == other.full_name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "<{} {}>".format(self.__class__.__name__, self.full_name)


def assert_cmd_exists(cmd):
    try:
        subprocess.check_output('which ' + cmd, shell=True)
    except subprocess.CalledProcessError:
        logging.critical("Command '{}' is not available".format(cmd))
        sys.exit(1)


class HgRepo(Repo):
    def __init__(self, *args, **kargs):
        Repo.__init__(self, *args, **kargs)
        assert_cmd_exists('hg')

    @classmethod
    def from_dir(cls, manager, dirname):
        repo = HgRepo(manager, full_name=None, dirname=dirname)
        origin = repo._get_origin_by_cmd()

        # FIXME: GitRepo
        if origin is None:
            raise exc.UnrelatedContent(dirname)

        repo.full_name = repo._get_full_name(origin)
        return repo

    def _build_api_repo(self):
        assert self.dirname is not None
        self._api_repo = hgapi.Repo(self.dirname)
        self._api_repo.hg_id()

    def _get_origin_sid(self, proto=PROTO_HTTPS):
        username = self.manager.session.account.username
        if proto == PROTO_SSH:
            username = 'hg'
            return 'ssh://{}@bitbucket.org/{}'.format(username, self.full_name)

        return 'https://{}@bitbucket.org/{}'.format(username, self.full_name)

    def _do_get_origin_by_cmd(self):
        return self.api_repo.hg_paths()['default']

    def _do_clone(self, proto, destdir):
        def local_changes():
            changes = self.api_repo.hg_status()
            if '?' in changes:
                del changes['?']
            return list(itertools.chain(*changes.values()))

        if not os.path.exists(destdir):
            origin = self._get_origin_by_rest(proto)
            origin = self._apply_pwd(origin)

            logger.debug("cloning %s", origin)
            hgapi.hg_clone(origin, destdir, *self._custom_args)
            return SyncStatus.CLONED

        if not os.path.isdir(destdir) or self != HgRepo.from_dir(self.manager, destdir):
            raise exc.UnrelatedContent(destdir)

        if local_changes():
            raise exc.UncommitedLocalChanges(destdir)

        return self.pull(proto)

    def pull(self, proto):
        origin = self._apply_pwd(self._get_origin_by_cmd(proto))

        try:
            self.api_repo.hg_command(*("incoming -q {}".format(origin).split()))
        except hgapi.hgapi.HgException:
            return SyncStatus.UPDATE

        self.api_repo.hg_pull(origin)
        self.api_repo.hg_update('tip')
        return SyncStatus.PULLED

    def push(self, proto):
        origin = self._apply_pwd(self._get_origin_by_cmd(proto))
        self.api_repo.hg_push(origin)

    def commited(self):
        out, err = hg_cmd(self.dirname, 'summary')
        commit = [line for line in out.split('\n') if line.startswith('commit:')][0]
        return '(clean)' in commit

    def pushed(self, tries=0):
        try:
            self.api_repo.hg_command('outgoing')
            return 'dirty'
        except hgapi.hgapi.HgException as e:
            error = str(e)
            if 'no changes found' in error:
                return 'synced'

            if 'repository does not exist' in error:
                return 'missing'

            if 'Connection reset by peer' in error:
                return 'cant-connect'

            print('\nwhen push {} ...'.format(self.dirname))
            print(e)
            return 'error'


class GitRepo(Repo):
    def __init__(self, *args, **kargs):
        Repo.__init__(self, *args, **kargs)
        assert_cmd_exists('git')

    @classmethod
    def from_dir(cls, manager, dirname):
        repo = GitRepo(manager, full_name=None, dirname=dirname)
        origin = repo._get_origin_by_cmd()
        repo.full_name = repo._get_full_name(origin)
        return repo

    def _build_api_repo(self):
        assert self.dirname is not None
        self._api_repo = gitapi.Repo(self.dirname)
        self._api_repo.git_command('remote', 'show', 'origin')

    def _get_origin_sid(self, proto=PROTO_HTTPS):
        if proto == PROTO_SSH:
            return 'ssh://git@bitbucket.org/{}.git'.format(self.full_name)

        return 'https://{}@bitbucket.org/{}.git'.format(self.manager.session.account.username, self.full_name)

    def _do_get_origin_by_cmd(self):
        remote = self.api_repo.git_command('remote', 'show', 'origin')
        prefix = 'Fetch URL: '

        retval = None
        for line in remote.split('\n'):
            line = line.strip()
            if line.startswith('Fetch'):
                i = line.index(prefix) + len(prefix)
                return line[i:]

        return retval

    @classmethod
    def _sanitize_full_name(cls, full_name):
        return full_name.strip('/')[:-4]

    def _do_clone(self, proto, destdir):
        def local_changes():
            changes = self.api_repo.git_status()
            if '??' in changes:
                del changes['??']
            return list(itertools.chain(*changes.values()))

        if not os.path.exists(destdir):
            origin = self._get_origin_by_rest(proto)
            origin = self._apply_pwd(origin)

            logger.debug("cloning %s", origin)
            gitapi.git_clone(origin, destdir)
            return SyncStatus.CLONED

        if not os.path.isdir(destdir) or self != GitRepo.from_dir(self.manager, destdir):
            raise exc.UnrelatedContent(destdir)

        if local_changes():
            raise exc.UncommitedLocalChanges(destdir)

        return self.pull(proto)

    def pull(self, proto):
        origin = self._apply_pwd(self._get_origin_by_cmd(proto))
        self.api_repo.git_fetch()
        if not self.api_repo.git_command(*("log ..origin".split())):
            return SyncStatus.UPDATE

        self.api_repo.git_pull(origin)
        return SyncStatus.PULLED

    def push(self, proto):
        origin = self._apply_pwd(self._get_origin_by_cmd(proto))
        self.api_repo.git_push(origin)

    def commited(self):
        # print "--- git commited", self.dirname
        out, err = git_cmd(self.dirname, 'status', '--porcelain')
        pending = [line for line in out.split('\n')
                   if line.strip() and not line.startswith('??')]
        # print pending, bool(pending)
        return not bool(pending)

    def pushed(self):
        try:
            out, err = git_cmd(self.dirname, 'push', '--dry-run')
            if 'Everything up-to-date' in err:
                return 'synced'
            else:
                return 'dirty'
        except gitapi.gitapi.GitException as e:
            if 'Could not read from remote repository' in str(e):
                return 'cant-connect'

            print('\nwhen push {} ...'.format(self.dirname))
            print(e)

        return 'error'


def check_full_name(full_name):
    msg = "repo name should match 'owner/slug' format"

    assert full_name.count('/') == 1, msg

    owner, slug = full_name.split('/')
    assert owner and slug, msg


class RepoManager(object):
    def __init__(self, account=None, num_workers=10):
        self.session = Session(account)
        self._keymanager = None
        self._pool = None
        self._num_workers = num_workers

    @property
    def pool(self):
        if self._pool is None:
            self._pool = SimpleThreadPool(self._num_workers)

        return self._pool

    def get_repo_info(self, full_name):
        return self.session.http_get('repositories/' + full_name)

    def get_repo_amount(self, owner):
        data = self.session.http_get('repositories/' + owner)
        return data['size']

    def list_repo_names(self, owner, step=lambda: None):
        def get_page_repo_names(url):
            "generate repository names for a single page"
            data = self.session.http_get(url)
            for k in data['values']:
                step()
                yield k['full_name']

        def async_get_page_repo_names(future):
            data = future.result().data
            for k in data['values']:
                step()
                yield k['full_name']

        def get_page_urls(url):
            "generate urls for each page (in paginated reply)"
            base = self.session.http_get(url)
            npages = 1 + (int(math.ceil(base['size'] // base['pagelen'])))

            for i in range(1, npages + 1):
                yield "{}?page={}".format(url, i)

        def threaded_page_request(url):
            urls = get_page_urls(url)
#            names_per_page = self.pool.map(get_page_repo_names, urls)

            futures = (self.session.async_get(u) for u in urls)
            names_per_page = self.pool.map(async_get_page_repo_names, futures)

            return itertools.chain(*names_per_page)

        return sorted(threaded_page_request('repositories/' + owner))

    def names2repos(self, names):
        return self.pool.map(functools.partial(Repo.from_remote, self), names)

    def names2repos2(self, names):
        urls = (bb_api2_uri('repositories/' + name) for name in names)
        futures = (self.session.async_get(url) for url in urls)
        return self.pool.map(functools.partial(Repo.from_remote_async, self), futures)

    def repo_list(self, owner, step=lambda: None):
        names = self.list_repo_names(owner, step)
        return self.names2repos2(names)

    def repo_create(self, full_name, scm='hg', is_private=True, description=''):
        check_full_name(full_name)

        data = dict(scm=scm,
                    is_private='true' if bool(is_private) else 'false',
                    description=description)

        self.session.http_post('repositories/' + full_name, data=data)

    def repo_delete(self, full_name):
        try:
            self.session.http_delete('repositories/' + full_name, ok=204)
        except exc.RemoteException as e:
            if e.reason == 'NOT_FOUND':
                raise exc.NoSuchRepo(full_name)
            raise

    @property
    def key_manager(self):
        if self._keymanager is None:
            self._keymanager = SshKeyManager(self.session)

        return self._keymanager


class SshKeyManager(object):
    def __init__(self, session):
        self.session = session

    def list_keys(self):
        return self.session.http_get(bb_api1_uri('ssh-keys'))

    def list_key_labels(self):
        return list(set([x['label'] for x in self.list_keys()]))

    def list_key_summaries(self):
        retval = []

        template = "pk: {pk:>8} |  label: {label:<12} |  {key_summary}"
        for key in self.list_keys():
            retval.append(template.format(
                label=key['label'],
                pk=key['pk'],
                key_summary=self._key_summary(key['key'])))

        return retval

    def _key_summary(self, keycontent):
        fields = keycontent.split()
        proto = seq = host = ''
        try:
            proto = fields[0]
            seq = fields[1]
            host = fields[2]
        except IndexError:
            pass

        return "{0} {1}...{2} {3}".format(proto, seq[:12], seq[-12:], host)

    def add_key(self, label, keyfile):
        try:
            retval = self.session.http_post(
                bb_api1_uri('ssh-keys'),
                data=dict(label=label, key=keyfile.read()))
        except exc.RemoteException as e:
            if e.reason.upper() == 'BAD_REQUEST':
                raise exc.NoValidKey()
            raise

        return retval['pk']

    def delete_key_by_label(self, label):
        keys = self.find_keys_by_label(label)
        if not keys:
            raise exc.NoSuchKey(label)

        for key in keys:
            self.delete_key_by_id(key['pk'])

    def delete_key_by_id(self, pk):
        self.session.http_delete(bb_api1_uri('ssh-keys/%s' % pk), ok=204)

    def find_keys_by_label(self, label):
        retval = []
        for key in self.list_keys():
            if key['label'] == label:
                retval.append(key)

        return retval
