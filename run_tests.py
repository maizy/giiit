#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

import sys
from os import path

import nose

if __name__ == '__main__':
    test_dir = path.join(path.dirname(__file__), 'tests')
    argv = sys.argv[:]
    argv.append(test_dir)
    for i in ['parser', 'logic']:  # tests dir
        argv.append(path.join(test_dir, i))
    nose.run_exit(argv=argv)
