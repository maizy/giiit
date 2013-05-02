# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.

import sys
from os import path

PY3 = sys.version_info[0] == 3
PY2 = not PY3
PY26 = sys.version_info < (2, 7)

if PY26:
    import unittest2 as unittest
else:
    import unittest

try:
    import giiit
    GIIIT_ROOT = path.abspath(path.dirname(giiit.__file__))
except ImportError:
    GIIIT_ROOT = path.abspath(path.join(path.dirname(__file__), '..', 'giiit'))

GIIIT_TESTS_ROOT = path.abspath(path.dirname(__file__))
