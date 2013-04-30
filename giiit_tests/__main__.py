# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

import sys
from os import path

import nose

if __name__ in ('__main__', 'giiit_tests.__main__'):
    test_dir = path.join(path.dirname(__file__))
    argv = sys.argv[:]
    argv.append(test_dir)
    nose.run_exit(argv=argv)
