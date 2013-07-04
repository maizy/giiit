# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

from os import path

from giiit_tests import unittest

from giiit.models import obj
from giiit.parsers import show as show_parser

resources = path.join(path.dirname(__file__), 'resources')


def read_resource(name):
    return open(path.join(resources, name)).read()


class ShowFormatRawTestCase(unittest.TestCase):
    def test_format_raw_commit(self):
        out = read_resource('show_format_raw_commit.out')
        expected = obj.Commit(ref='f0c28d2215ec95956dfab156e3aa36a362b81c73',
                                  tree_ref='fd16a5e33c0c0f4488a8ee6fde8c9a5344cbef9e',
                                  parent_refs=['965263cde4fe43f536e6a07d2d247c23c8737c42'],
                                  author_raw='Nikita Kovaliov <nikita@maizy.ru> 1362315523 +0400',
                                  committer_raw='Nikita Kovaliov <nikita@maizy.ru> 1362315523 +0400')
        real = show_parser.format_raw(out)
        self.assertEqual(expected, real)
