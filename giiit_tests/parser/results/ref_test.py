# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

from giiit_tests import unittest

from giiit.parsers import WrongOutputError, ParserError
from giiit.parsers.results import ref


class SymbolicRefTestCase(unittest.TestCase):

    def test_full(self):
        full = 'refs/heads/master'
        r = ref.SymbolicRef(full)
        self.assertEqual(r.full, full)
        with self.assertRaises(AttributeError):
            r.full = 'refs/heads/br'
            del r.full

    def test_short(self):
        r = ref.SymbolicRef('refs/heads/master')
        self.assertEqual(r.short, 'master')
        with self.assertRaises(AttributeError):
            r.short = 'br'
            del r.short

    def test_get_type(self):
        r = ref.SymbolicRef('refs/heads/master')
        self.assertEqual(r.get_type(), 'heads')

    def test_get_wrong_type_value(self):
        r = ref.SymbolicRef('refs/oops/master')
        with self.assertRaises(ParserError):
            r.get_type()

    def test_get_wrong_type_format(self):
        r = ref.SymbolicRef('refs-heads-master')
        with self.assertRaises(WrongOutputError):
            r.get_type()
