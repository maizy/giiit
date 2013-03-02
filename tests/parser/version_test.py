# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

import unittest

from giiit.parsers import WrongOutputError
from giiit.parsers import version


class VersionTestCase(unittest.TestCase):
    def test_version(self):
        output = 'git version 1.8.1.1\n'
        expected = version.Version(version='1.8.1.1', parts=['1', '8', '1', '1'],
                                   major=1, minor=8)
        real = version.version(output)
        self.assertEqual(expected, real)

    def test_wrong_version_output(self):
        output = 'Mercurial Distributed SCM (version 2.0.2)'
        with self.assertRaises(WrongOutputError):
            version.version(output)

    def test_version_compairing(self):
        output = 'git version 1.8.1.1\n'
        output2 = 'git version 1.7\n'
        self.assertEqual(version.version(output), version.version(output))
        self.assertLess(version.version(output2), version.version(output))
