# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals

import re

_strip_regexp = re.compile(r'^#.*$\n?', re.UNICODE | re.MULTILINE)

def strip_comments(output):
    return re.sub(_strip_regexp, '', output)
