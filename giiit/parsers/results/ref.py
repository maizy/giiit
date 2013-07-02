# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

from giiit.parsers import ParserError, WrongOutputError

SYMBOLIC_REF_TYPES = ('tags', 'heads', 'remotes')


class SymbolicRef(object):

    def __init__(self, full):
        self._full = full

        parts = self._full.rsplit('/', 1)
        self._short = parts[1] if len(parts) == 2 else None

    @property
    def short(self):
        return self._short

    @property
    def full(self):
        return self._full

    def get_type(self):
        parts = self.full.split('/', 2)
        if len(parts) != 3 or (len(parts) > 0 and parts[0] != 'refs'):
            raise WrongOutputError('Wrong ref "{0}"'.format(self.full))
        type_ = parts[1]
        if type_ not in SYMBOLIC_REF_TYPES:
            raise ParserError('Unknown ref type "{0}"'.format(type_))
        return type_

    def is_tag(self):
        return self.get_type() == 'tags'

    def is_remote(self):
        return self.get_type() == 'remotes'

    def is_head(self):
        return self.get_type() == 'heads'
