# -*- coding:utf-8; tab-width:4; mode:python -*-

import itertools
from functools import reduce


def uniq(alist):
    '''
    >>> list(uniq([1, 2, 2, 3, 2, 3, 5]))
    [1, 2, 3, 5]
    '''

    s = set()
    for i in alist:
        if i in s:
            continue

        s.add(i)
        yield i


def merge(*args):
    """
    >>> merge([1,2], [2,4], [5, 6])
    [1, 2, 2, 4, 5, 6]
    >>> merge([[1,2], [2,4]])
    [[1, 2], [2, 4]]
    >>> merge(*[[1,2], [2,4]])
    [1, 2, 2, 4]
    """
    return reduce(list.__add__, args, list())


def merge_uniq(*args):
    """
    >>> merge_uniq([1,2], [2,4], [5, 6])
    [1, 2, 4, 5, 6]
    >>> merge_uniq([1,2])
    [1, 2]
    >>> merge_uniq(*[[1,2], [2,4]])
    [1, 2, 4]
    >>> merge_uniq([1, 2, 2, 3, 2, 3, 5])
    [1, 2, 3, 5]
    """
    return list(set(merge(*args)))


def striplit(val, sep=' ', require_len=None):
    '''
    >>> striplit(" this -  is a -  sample  ", sep='-')
    ['this', 'is a', 'sample']
    '''

    val = val.strip(sep)
    retval = [x.strip() for x in val.split(sep)]
    if require_len is not None and len(retval) != require_len:
        raise ValueError("Incorrect size != %s" % require_len)
    return retval


def split_if(seq, pred):
    """
    Split an iterable based on the a predicate.
    url: http://stackoverflow.com/questions/949098/python-split-a-list-based-on-a-condition

    >>> split_if(['a', '2', 'c', 'z', '5'], str.isdigit)
    [['2', '5'], ['a', 'c', 'z']]
    """

    retval = []
    for key, group in itertools.groupby(
        sorted(seq, key=pred, reverse=True), key=pred):
        retval.append(list(group))
    return retval
