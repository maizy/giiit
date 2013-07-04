# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

from giiit_tests import unittest

from giiit.parsers import WrongOutputError, ParserError
from giiit.models import ref
from giiit.multi_version import uu


class SymbolicRefTestCase(unittest.TestCase):

    def test_to_str(self):
        full = 'refs/heads/master'
        r = ref.SymbolicRef(full)
        self.assertEqual(uu(r), full)

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
        with self.assertRaises(ParserError) as raise_context:
            r.get_type()
        self.assertEqual(uu(raise_context.exception), 'Unknown ref type "oops"')

    def test_get_wrong_type_format(self):
        r = ref.SymbolicRef('refs-heads-master')
        with self.assertRaises(WrongOutputError) as raise_context:
            r.get_type()
        self.assertEqual(uu(raise_context.exception), 'Wrong ref "refs-heads-master"')
