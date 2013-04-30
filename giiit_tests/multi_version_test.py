# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

from giiit_tests import unittest

from giiit.multi_version import to_str, PY2, PY3


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
            self.skipTest('Python 2 only test')
        obj = self.test_class()
        self.assertEqual(self.expected_results, str(obj))
