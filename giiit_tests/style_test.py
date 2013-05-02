# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# Based on https://gist.github.com/mitechie/3436363
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

from os import path
import pep8

from giiit_tests import unittest, GIIIT_ROOT, GIIIT_TESTS_ROOT

src_dirs = [GIIIT_ROOT, GIIIT_TESTS_ROOT]


class StyleTestCase(unittest.TestCase):
    def test_pep8(self):
        pep8style = pep8.StyleGuide(
            show_pep8=False,
            show_source=True,
            repeat=True,
            max_line_length=119,
            statistics=True,
        )
        result = pep8style.check_files(src_dirs)
        if result.total_errors > 0:
            print('\nStatistics:')
            result.print_statistics()
            self.fail('PEP8 styles errors')
