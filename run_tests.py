#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.

import runpy
import sys
if sys.version_info < (2, 7):
    runpy.run_module('giiit_tests.__main__')
else:
    runpy.run_module('giiit_tests')
