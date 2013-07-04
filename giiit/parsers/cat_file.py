# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

from giiit.parsers import simple_output, WrongOutputError
from giiit.models import obj


def t(output, check_type=True):
    """
    show object type identified
    `git cat-file -b REF`
    """
    output = simple_output(output)
    if check_type and output not in obj.TYPES:
        raise WrongOutputError('Unknown type {0}'.format(output))
    return output
