# -*- coding:utf-8; tab-width:4; mode:python -*-

from commodity.pattern import MetaBunch


class BasicException(Exception):
    def __str__(self):
        msg = Exception.__str__(self)
        if not msg.strip():
            msg = self.message

        return msg


class BucketException(BasicException):
    def __str__(self):
        msg = BasicException.__str__(self)
        return 'error: %s: %s' % (self.__class__.__name__, msg)


class RemoteException(BasicException):
    def __init__(self, url, reason='', msg='', detail=''):
        self.url = url
        self.reason = reason
        self.message = reason
        more = ("{}\n{}".format(msg, detail)).strip()
        if more:
            self.message = "url: {}\n  {}: {}".format(url, self.message, more)

    @classmethod
    def from_reply(cls, reply):
        try:
            data = MetaBunch(reply.json())
        except ValueError:
            data = {}

        # print reply
        # print "dir:", dir(reply)
#        print "content:", reply.content
        # print "elapsed:", reply.elapsed
        # print "reason:", reply.reason
        # print "text:", reply.text
        # print "request:", reply.request
        # # print "raise_for_status:", reply.raise_for_status()

        msg = detail = ''
        error = data.get('error', '')
        if error:
            msg = error.get('message', '')
            detail = error.get('detail', '')

        return RemoteException(reply.request.url,
                               str(reply.reason).replace(' ', '_'),
                               msg, detail)

    def __str__(self):
        msg = BasicException.__str__(self)
        return 'bitbucket.org remote error:\n  %s' % (msg)


class InvalidCredentials(BucketException): pass
class RepositoryNotFound(BucketException): pass
class ServiceUnavailable(BucketException): pass
class UnrelatedContent(BucketException): pass
class NoSuchUser(BucketException): pass
class AuthenticationError(BucketException): pass
class NoBitbucketRepo(Exception): pass


class OwnerRequired(BucketException):
    message = "Must specify an account or repository owner"

class WrongRepoPathFormat(BucketException):
    message = "Wrong repository path format. It should match [owner]/repository_name"

class CloneError(BucketException): pass

class NoSuchRepo(BucketException): pass
class NoSuchKey(BucketException): pass

class NoValidKey(BucketException): pass
class UncommitedLocalChanges(BucketException): pass
