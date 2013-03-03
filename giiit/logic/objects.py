# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

from giiit.cmd_builders import show as show_cmd_builder
from giiit.parsers import show as show_parser


def is_commit(ref, helper):
    """
    @type ref: C{str} - object hash or ref name
    @type helper: git helper function
    @rtype: C{bool}

    helper(git_command_params) => (return_code, output)
    """
    ret_code, output = helper(show_cmd_builder.object_info(ref))
    ret_code = int(ret_code)
    if ret_code != 0:
        return False
    parsed_info = show_parser.format_raw(output)
    if parsed_info.type != 'commit':
        return False
    return True
