# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

from giiit.parsers import ParserError, WrongOutputError
from giiit.multi_version import to_str, uu

SYMBOLIC_REF_TYPES = ('tags', 'heads', 'remotes')


@to_str
class Ref(object):

    def __init__(self, ref):
        self._ref = ref

    def to_str(self):
        return self._ref


class SymbolicRef(Ref):

    def __init__(self, full):
        super(SymbolicRef, self).__init__(full)
        parts = uu(self).rsplit('/', 1)
        self._short = parts[1] if len(parts) == 2 else None

    @property
    def short(self):
        return self._short

    def get_type(self):
        parts = uu(self).split('/', 2)
        if len(parts) != 3 or (len(parts) > 0 and parts[0] != 'refs'):
            raise WrongOutputError('Wrong ref "{0!s}"'.format(self))
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
