# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

from collections import namedtuple

from giiit.multi_version import total_ordering, to_str


@to_str
@total_ordering
class Version(namedtuple('_Version', ['version', 'parts', 'major', 'minor'])):

    def to_str(self):
        return 'Version {0}'.format(self.version)

    def __eq__(self, other):
        return self.version == other.version

    def __le__(self, other):
        return self.parts < other.parts
