# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals

import re

_strip_regexp = re.compile(r'^#.*$\n?', re.UNICODE | re.MULTILINE)


def strip_comments(output):
    return re.sub(_strip_regexp, '', output)


def namedtuple_with_defaults(_type, _default_value=None, **kwargs):
    """
    Construct nametuple instance with default value for all args not
    included in kwargs.
    """
    args_list = _type._fields
    params = dict([(x, _default_value) for x in args_list])
    params.update(kwargs)
    return _type(**params)
