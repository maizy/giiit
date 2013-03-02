# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# Based on https://gist.github.com/mitechie/3436363
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

from os import path
import unittest
from StringIO import StringIO

import pep8
from pyflakes.scripts.pyflakes import checkRecursive as pyflakes_check
from pyflakes.reporter import Reporter as PyFlakesReporter


project_root = path.abspath(path.join(path.dirname(__file__), '..'))
src_dirs = [path.join(project_root, 'giiit'),
            path.join(project_root, 'tests')]


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


class PyFlakesTestCase(unittest.TestCase):

    def test_pyflakes(self):
        warn_stream = StringIO()
        err_stream = StringIO()
        reporter = PyFlakesReporter(warn_stream, err_stream)
        warnings = pyflakes_check(src_dirs, reporter)
        if warnings > 0:
            err = err_stream.getvalue()
            warn = warn_stream.getvalue()
            report = []
            if err:
                report.append('PyFlake errors: {0}'.format(err))
            if warn:
                report.append('PyFlake warnings: {0}'.format(warn))
            self.fail('\n\n'.join(report))
