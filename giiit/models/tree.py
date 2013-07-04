# _*_ coding: utf-8 _*_# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

from collections import namedtuple

STATUS_CODES = {
    ' ': 'unmodified',
    'M': 'modified',
    'A': 'added',
    'D': 'deleted',
    'R': 'renamed',
    'C': 'copied',
    'U': 'unmerged',
    '?': 'untracked',
    '!': 'ignored',
}

Entity = namedtuple('Entity', ['work_tree_status_code', 'work_tree_status', 'index_status_code', 'index_status',
                               'path', 'new_path'])
