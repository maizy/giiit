# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

from collections import namedtuple

from giiit_tests import unittest

from giiit.utils import strip_comments, namedtuple_with_defaults


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

    def namedtuple_defaults_test(self):
        nt = namedtuple('nt', 'a b c d')
        expected = nt(a=1, b=None, c=3, d=None)
        real = namedtuple_with_defaults(nt, c=3, a=1)
        self.assertEqual(expected, real)
