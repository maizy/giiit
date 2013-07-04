# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

from giiit_tests import unittest

from giiit.multi_version import to_str, PY2, PY3, uu


class ToStrDecoratorTestCase(unittest.TestCase):
    def setUp(self):
        results = 'Hello=\u043f\u0440\u0438\u0432\u0435\u0442.'

        @to_str
        class SomeClass(object):
            def to_str(self):
                return results

        self.expected_results = results
        self.test_class = SomeClass

    def test_stringify_py2(self):
        if not PY2:
            self.skipTest('Python 2 only test')
        obj = self.test_class()
        self.assertEqual(self.expected_results, unicode(obj))

    def test_stringify_py3(self):
        if not PY3:
            self.skipTest('Python 3 only test')
        obj = self.test_class()
        self.assertEqual(self.expected_results, str(obj))


class UuTestCase(unittest.TestCase):

    def test_stringify_py2(self):
        if not PY2:
            self.skipTest('Python 2 only test')

        expected_results = 'Hello=\u043f\u0440\u0438\u0432\u0435\u0442.'

        class ToUnicodeClass(object):
            def __unicode__(self):
                return expected_results

            def __repr__(self):
                return 'bu-bu'

            def __str__(self):
                return str('str')

        obj = ToUnicodeClass()
        self.assertEqual(uu(obj), expected_results)
        self.assertEqual(type(uu(obj)), unicode)
        self.assertEqual('{0}'.format(obj), expected_results)
        self.assertEqual('{0!s}'.format(obj), expected_results)

    def test_stringify_py3(self):
        if not PY3:
            self.skipTest('Python 3 only test')

        expected_results = 'Hello=\u043f\u0440\u0438\u0432\u0435\u0442.'

        class ToStrClass(object):
            def __str__(self):
                return expected_results

            def __repr__(self):
                return 'bu-bu'

        obj = ToStrClass()
        self.assertEqual(uu(obj), expected_results)
        self.assertEqual(type(uu(obj)), str)
        self.assertEqual('{0}'.format(obj), expected_results)
        self.assertEqual('{0!s}'.format(obj), expected_results)
