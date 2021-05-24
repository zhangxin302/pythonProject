#!/usr/bin/python
# -*- coding:utf-8; tab-width:4; mode:python -*-

import os
import io
import stat
import time
import errno

from commodity.pattern import Bunch


try:
    from collections import OrderedDict
except ImportError:
    from pyarco.Type import SortedDict as OrderedDict


class BaseFS:
    def resolve(self, path):
        if os.path.isabs(path):
            return path

        return self.find(path)[0]

    def find(self, target, prefix=''):
        full = os.path.join(prefix, target)
        if not self.exists(full):
            e = OSError()
            e.errno = 2
            e.strerror = "No such file or directory"
            e.filename = target
            raise e

        return [full]

    def split(self, path):
        if not path:
            return []

        return path.strip(os.sep).split(os.sep)

    @staticmethod
    def clean_path(path):
        if not path:
            return ''

        return path.strip(os.sep)

    @staticmethod
    def oserror(msg, fpath, errno):
        retval = OSError()
        retval.strerror = msg
        retval.filename = fpath
        retval.errno = errno
        return retval

    @staticmethod
    def ioerror(msg, fpath, errno):
        retval = IOError()
        retval.strerror = msg
        retval.filename = fpath
        retval.errno = errno
        return retval

    @staticmethod
    def no_such_file(path):
        return BaseFS.oserror("No such file or directory", path, errno.ENOENT)

    @staticmethod
    def file_exists(path):
        return BaseFS.oserror("File exists", path, errno.EEXIST)


class ActualFileSystem(BaseFS):
    def __init__(self, base):
        self.base = base

    def open(self, fname, mode='r'):
        return open(fname, mode)

    def mkdir(self, path):
        os.mkdir(path)

    def makdirs(self, path):
        os.makedirs(path)


class FakeStat(Bunch):
    def __init__(self, *args, **kargs):
        self.st_mode = None
        self.st_ino = 0
        self.st_dev = 0
        self.st_nlink = None
        self.st_uid = 0
        self.st_gid = 0
        self.st_size = 0
        self.st_atime = 0
        self.st_mtime = 0
        self.st_ctime = 0

        super(FakeStat, self).__init__(*args, **kargs)


class FakeDirectory(dict):
    def __init__(self, path):
        self.path = path
        super(FakeDirectory, self).__init__()
        self.stat_data = FakeStat(st_mode = stat.S_IFDIR | 0o755, st_nlink = 2)

    def update_stat(self):
        pass

    def checked_run(self, func, path):
        path = BaseFS.clean_path(path)
        try:
            return func(path)
        except KeyError:
            raise BaseFS.no_such_file(path)

    def get_node(self, path):
        path = BaseFS.clean_path(path)
        head, tail = self.split_first(path)
        if tail:
            return self[head].get_node(tail)

        return self[head]

    def exists(self, path):
        try:
            self.get_node(path)
        except KeyError:
            return False

        return True

    def ls(self, path=''):
        path = BaseFS.clean_path(path)
        if not path:
            keys = list(self.keys())
            if '' in keys:
                keys.remove('')
            return keys

        head, tail = self.split_first(path)
        return self[head].ls(tail)

    def mkdir(self, path):
        path = BaseFS.clean_path(path)

        if not path:
            raise BaseFS.no_such_file(path)

        head, tail = self.split_first(path)
        if head in self:
            if not tail:
                raise BaseFS.file_exists(path)
        else:
            self[head] = FakeDirectory(os.path.join(self.path, path))

        if tail:
            self[head].mkdir(tail)

    def makedirs(self, path):
        current = ""
        for dname in os.path.split(path):
            current = os.path.join(current, dname)
            try:
                self.mkdir(current)
            except OSError:
                pass

    def move(self, old, new):
        old_dir, old_file = os.path.split(BaseFS.clean_path(old))
        new_dir, new_file = os.path.split(BaseFS.clean_path(new))
        self[new_dir][new_file] = self[old_dir][old_file]
        self.remove(old)

    def open(self, path, mode='r'):
        def __open(path):
            head, tail = self.split_first(path)

            if tail:
                return self[head].open(tail, mode)

            if 'r' in mode:
                return self[head]

            if 'w' in mode:
                self[head] = FakeFile(os.path.join(self.path, path))
                return self[head]

        return self.checked_run(__open, path)

    def remove(self, path):
        def __remove(path):
            head, tail = self.split_first(path)

            if tail:
                return self[head].remove(tail)

            del self[head]

        return self.checked_run(__remove, path)

    def rmdir(self, path):
        def __rmdir(path):
            if not path:
                raise BaseFS.no_such_file(path)

            head, tail = self.split_first(path)
            if tail:
                return self[head].rmdir(tail)

            del self[head]

        return self.checked_run(__rmdir, path)

    def stat(self, path=''):
        def __stat(path):
            head, tail = self.split_first(path)
            if tail:
                return self[head].stat(tail)

            self[head].update_stat()
            return self[head].stat_data

        return self.checked_run(__stat, path)

    @classmethod
    def split_first(cls, path):
        if not path:
            return '', ''

        try:
            head, tail = path.split(os.sep, 1)
        except ValueError:
            return path, ''

        return head, tail


class FakeFile(io.BytesIO):
    def __init__(self, path, content=b''):
        self.path = path
        super(FakeFile, self).__init__(content)
        now = int(time.time())
        self.stat_data = FakeStat(st_mode = stat.S_IFREG | 0o666,  # rw- rw- rw-
                                  st_nlink = 1,
                                  st_size = self.size(),
                                  st_ctime = now,
                                  st_mtime = now)

    def update_stat(self):
        self.stat_data.st_size = self.size()

    def size(self):
        return len(self.getvalue())

    def close(self):
        self.seek(0)

    def __repr__(self):
        return "<FakeFS.File '{0}' {1}>".format(self.path, id(self))


class FakeFS(FakeDirectory, BaseFS):
    def __init__(self):
        super(FakeFS, self).__init__(os.sep)
        self[''] = self

    def listdir(self, path=''):
        if path == os.sep:
            path = ''

        return self.ls(path)
