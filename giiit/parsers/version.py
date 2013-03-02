# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

import re
from collections import namedtuple
from functools import total_ordering
from distutils.version import LooseVersion as _LooseVersion

from giiit.parsers import WrongOutputError


@total_ordering
class Version(namedtuple('_Version', ['version', 'parts', 'major', 'minor'])):
    def __unicode__(self):
        return 'Version {0}'.format(self.version)

    def __eq__(self, other):
        return _LooseVersion(self.version) == _LooseVersion(other.version)

    def __le__(self, other):
        return _LooseVersion(self.version) < _LooseVersion(other.version)


def version(output):
    """
    `git --version` > git version 1.8.1.1
    """
    output = output.rstrip()
    words = re.split('\s+', output, 3)
    if not words or words[0] != 'git' or words[1] != 'version':
        raise WrongOutputError()
    version = words[2]
    parts = version.split('.')
    try:
        major = int(parts[0]) if len(parts) > 0 else None
    except ValueError:
        major = None
    try:
        minor = int(parts[1]) if len(parts) > 1 else None
    except ValueError:
        minor = None
    return Version(version, parts, major, minor)