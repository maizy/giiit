# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import


class ParserError(Exception):
    pass


class WrongOutputError(ParserError):
    pass
