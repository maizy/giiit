# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

from giiit.multi_version import uu

from giiit.models import ref


def symbolic_ref(output):
    output = uu(output)
    return ref.SymbolicRef(output)
