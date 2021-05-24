# -*- coding: utf-8; mode: python -*-

# urlparse utils

import urlparse


def parse(url):
    retval = urlparse.urlparse(url)
    if not retval.scheme and url.startswith('git@'):
        url = url.replace(':', '/')
        url = 'git://' + url
        # print("--", url)
        return urlparse.urlparse(url)

    return retval


def change_login(url, user='', password=''):
    """
    >>> change_login(urlparse.urlparse("http://guido@www.cwi.nl:80/python.html")
    >>> _.geturl()
    'http://www.cwi.nl:80/python.html'
    """

    user = user or ''
    password = password or ''
    parts = list(urlparse.urlsplit(url.geturl()))

    user_pwd = user + ':' + password
    user_pwd = user_pwd.strip(':')
    user_pwd = user_pwd + '@' if user else ''

    parts[1] = user_pwd + url.hostname
    return urlparse.urlparse(urlparse.urlunsplit(parts))


def change_proto(url, proto):
    """
    >>> change_proto(urlparse.urlparse("http://hostname.net/path"), "ssh")
    >>> _.geturl()
    "ssh://hostname.net/path"
    """
    parts = list(urlparse.urlsplit(url.geturl()))
    parts[0] = proto
    return urlparse.urlparse(urlparse.urlunsplit(parts))
