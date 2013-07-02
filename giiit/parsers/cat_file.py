# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

from giiit.parsers import simple_output, WrongOutputError
from giiit.parsers.results import objects


def t(output):
    """
    show object type identified
    `git cat-file -b REF`
    """
    output = simple_output(output)
    if output not in objects.TYPES:
        raise WrongOutputError('Unknown type {0}'.format(output))
    return output
