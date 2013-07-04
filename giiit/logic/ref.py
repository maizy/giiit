# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

from giiit.multi_version import uu
from giiit.cmd_builders import cat_file as cat_file_builders
from giiit.parsers import cat_file as cat_file_parsers
from giiit.utils import call_helper


def _get_type(ref, helper):
    ref = uu(ref)
    cmd = cat_file_builders.t(ref)
    res = call_helper(helper, cmd)
    return cat_file_parsers.t(res.out, check_type=False) if res.code == 0 else None


def is_exists(ref, helper):
    """
    @type ref: C{str} or L{giiit.models.obj.Ref} - object hash, ref name or Ref object
    @type helper: git helper function
    @rtype: C{bool}
    """
    return _get_type(ref, helper) is not None


def is_commit(ref, helper):
    """
    @type ref: C{str} or L{giiit.models.obj.Ref} - object hash, ref name or Ref object
    @type helper: git helper function
    @rtype: C{bool}
    """
    return _get_type(ref, helper) == 'commit'


def is_blob(ref, helper):
    """
    @type ref: C{str} or L{giiit.models.obj.Ref} - object hash, ref name or Ref object
    @type helper: git helper function
    @rtype: C{bool}
    """
    return _get_type(ref, helper) == 'blob'


def is_tree(ref, helper):
    """
    @type ref: C{str} or L{giiit.models.obj.Ref} - object hash, ref name or Ref object
    @type helper: git helper function
    @rtype: C{bool}
    """
    return _get_type(ref, helper) == 'tree'
