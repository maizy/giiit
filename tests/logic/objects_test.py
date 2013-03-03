# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

import unittest
from os import path

from giiit.logic import objects as objects_logic

resources = path.join(path.dirname(__file__), '..', 'parser', 'resources')


def read_resource(name):
    return open(path.join(resources, name)).read()


def stub_helper(ret_code, stub_resource_name=None, expected_args=None):
    def _helper(args):
        if expected_args is not None and expected_args != args:
            raise AssertionError('args not matched {0!r} != {1!r}'.format(args, expected_args))
        if stub_resource_name is not None:
            output = read_resource(stub_resource_name)
        else:
            output = ''
        return ret_code, output
    return _helper


class IsCommitTestCase(unittest.TestCase):
    def test_is_commit(self):
        ref = 'f0c28d2215ec95956dfab156e3aa36a362b81c73'
        helper = stub_helper(0, 'show_format_raw_commit.out', expected_args=['show', '--format=raw', ref])
        self.assertTrue(objects_logic.is_commit(ref, helper))
