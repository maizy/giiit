# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

from giiit_tests import unittest

from giiit.parsers import WrongOutputError
from giiit.parsers.version import version as version_parser
from giiit.models import Version


class VersionTestCase(unittest.TestCase):

    def test_version(self):
        output = 'git version 1.8.1.1\n'
        expected = Version(version='1.8.1.1', parts=['1', '8', '1', '1'],
                           major=1, minor=8)
        real = version_parser(output)
        self.assertEqual(expected, real)

    def test_wrong_version_output(self):
        output = 'Mercurial Distributed SCM (version 2.0.2)'
        with self.assertRaises(WrongOutputError):
            version_parser(output)

    def test_version_compairing(self):
        v1_8_1_1 = 'git version 1.8.1.1\n'
        v1_8 = 'git version 1.8\n'
        v1_7 = 'git version 1.7\n'
        self.assertEqual(version_parser(v1_8_1_1), version_parser(v1_8_1_1))
        self.assertLess(version_parser(v1_7), version_parser(v1_8_1_1))
        self.assertLess(version_parser(v1_8), version_parser(v1_8_1_1))
        self.assertGreater(version_parser(v1_8_1_1), version_parser(v1_7))
        self.assertGreater(version_parser(v1_8), version_parser(v1_7))
