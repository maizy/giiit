# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

from os import path

from giiit_tests import unittest

from giiit.logic import ref as ref_logic

resources = path.join(path.dirname(__file__), '..', 'parser', 'resources')


def stub_helper(code, out, err='', expected_args=None):
    def _helper(args):
        if expected_args is not None and expected_args != args:
            raise AssertionError('args not matched {0!r} != {1!r}'.format(args, expected_args))
        return code, out, err
    return _helper


class RefLogicTestCase(unittest.TestCase):

    def test_is_commit(self):
        ref = 'f0c28d2215ec95956dfab156e3aa36a362b81c73'
        helper = stub_helper(code=0, out='commit\n', expected_args=['cat-file', '-t', ref])
        self.assertTrue(ref_logic.is_commit(ref, helper))

    def test_is_exists(self):
        ref1 = 'notexists'
        helper1 = stub_helper(code=128, out='', expected_args=['cat-file', '-t', ref1],
                              err='fatal: Not a valid object name {0}'.format(ref1))
        self.assertFalse(ref_logic.is_exists(ref1, helper1))

        ref2 = 'f0c28d2215ec95956dfab156e3aa36a362b81c73'
        helper2 = stub_helper(code=0, out='commit\n')
        self.assertTrue(ref_logic.is_exists(ref2, helper2))
