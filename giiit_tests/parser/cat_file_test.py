# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

from giiit_tests import unittest

from giiit.parsers import WrongOutputError
from giiit.parsers import cat_file


class CatFileTCase(unittest.TestCase):

    def test_known_types(self):
        for status in ('commit', 'tree', 'tag', 'blob'):
            self.assertEqual(cat_file.t('{0}\n'.format(status)), status)

    def test_unknown_types(self):
        for output in ('blabla\n', ' \n', '\n', None, ''):
            with self.assertRaises(WrongOutputError):
                cat_file.t(output)
