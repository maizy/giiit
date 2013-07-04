# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals

from collections import namedtuple
import re

from giiit import Error
from giiit.multi_version import uu, to_uu

_strip_comments_regexp = re.compile(r'^#.*$\n?', re.UNICODE | re.MULTILINE)


def strip_comments(output):
    return re.sub(_strip_comments_regexp, '', output)


def namedtuple_with_defaults(_type, _default_value=None, **kwargs):
    """
    Construct nametuple instance with default value for all args not
    included in kwargs.
    """
    args_list = _type._fields
    params = dict([(x, _default_value) for x in args_list])
    params.update(kwargs)
    return _type(**params)

HelperResults = namedtuple('HelperResults', ['code', 'out', 'err'])


def call_helper(helper, git_cmd):
    if not callable(helper):
        raise Error('Helper not callable')

    try:
        res = helper(git_cmd)
    except Exception as e:
        raise Error("Error on helper's call. Helper raises exception: {0}.".format(e))

    if not isinstance(res, tuple) or len(res) != 3:
        raise Error('Helper results should be tuple of three elements')

    code, out, err = res
    try:
        code = int(code)
    except TypeError as e:
        raise Error("Couldn't convert result code to int. {0}".format(e))

    try:
        out = to_uu(out) if out is not None else ''
        err = to_uu(err) if err is not None else ''
    except (TypeError, UnicodeError) as e:
        raise Error("Couldn't convert stdout or stderr to string. {0}".format(e))

    return HelperResults(code, out, err)
