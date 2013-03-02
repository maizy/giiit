# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

import unittest

from giiit.parsers.utils import strip_comments


class UtilsTestCase(unittest.TestCase):
    def test_strip_comments(self):
        output = '''\
#some comment
# some comment 2 #
#
##

normal text
not # a comment
# end comment

'''

        expected = '''\

normal text
not # a comment

'''
        real = strip_comments(output)
        self.assertEqual(expected, real)
