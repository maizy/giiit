# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

from giiit import Exception
from giiit.multi_version import uu


class ParserError(Exception):
    pass


class WrongOutputError(ParserError):
    pass


def simple_output(output):
    output = uu(output)
    return output.strip()
