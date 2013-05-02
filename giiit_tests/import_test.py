# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# Based on https://gist.github.com/mitechie/3436363
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

import os
from os import path

from giiit_tests import unittest, GIIIT_ROOT, PY26

if PY26:
    def import_module(name):
        return __import__(name, globals(), {}, [], -1)
else:
    from importlib import import_module


class ImportTestCase(unittest.TestCase):

    def test_import_main_module(self):
        import giiit

    def test_import_all_sumbmodules(self):
        init = '.__init__'
        init_len = len(init)
        for dirpath, _, filenames in os.walk(GIIIT_ROOT):
            for file in filenames:
                full_path = path.join(dirpath, file)
                if full_path.endswith('.py') and full_path.startswith(GIIIT_ROOT + '/'):
                    module_name = full_path[len(GIIIT_ROOT)+1:-3].replace('/', '.')
                    if module_name == '__init__':
                        continue
                    if module_name.endswith(init):
                        module_name = module_name[:-init_len]
                    module_name = 'giiit.{0}'.format(module_name)
                    self.assertModuleImports(module_name)

    def assertModuleImports(self, name):
        try:
            import_module(name)
        except ImportError:
            self.fail('Unable to import module {0}'.format(name))
