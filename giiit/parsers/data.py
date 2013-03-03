# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

GIT_OBJECTS_TYPES = ['commit', 'tree', 'tag', 'blob']

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
