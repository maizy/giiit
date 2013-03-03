# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

import unittest
from os import path

from giiit.parsers import status

resources = path.join(path.dirname(__file__), 'resources')


class StatusParserTestCase(unittest.TestCase):
    def setUp(self):
        self.z_output = open(path.join(resources, 'status_z_porcelain.out')).read()

    def test_porcelain_z(self):
        expected = [

            status.Entity(
                work_tree_status_code=' ',
                work_tree_status=status.STATUS_CODES[' '],
                index_status_code='A',
                index_status=status.STATUS_CODES['A'],
                path='.gitignore',
                new_path=None),

            status.Entity(
                work_tree_status_code=' ',
                work_tree_status=status.STATUS_CODES[' '],
                index_status_code='R',
                index_status=status.STATUS_CODES['R'],
                path='B',
                new_path='BB')
        ]
        real = status.porcelain_z(self.z_output)
        self.assertListEqual(expected, real)
