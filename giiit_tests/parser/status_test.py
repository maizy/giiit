# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

from os import path

from giiit_tests import unittest

from giiit.parsers import status
from giiit.parsers.results import Entity
from giiit.parsers.data import STATUS_CODES

resources = path.join(path.dirname(__file__), 'resources')


class StatusParserTestCase(unittest.TestCase):
    def setUp(self):
        self.z_output = open(path.join(resources, 'status_z_porcelain.out')).read()

    def test_porcelain_z(self):
        expected = [

            Entity(
                work_tree_status_code=' ',
                work_tree_status=STATUS_CODES[' '],
                index_status_code='A',
                index_status=STATUS_CODES['A'],
                path='.gitignore',
                new_path=None),

            Entity(
                work_tree_status_code=' ',
                work_tree_status=STATUS_CODES[' '],
                index_status_code='R',
                index_status=STATUS_CODES['R'],
                path='B',
                new_path='BB')
        ]
        real = status.porcelain_z(self.z_output)
        self.assertListEqual(expected, real)
