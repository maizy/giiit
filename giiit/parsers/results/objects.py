# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

TYPES = ['commit', 'tree', 'tag', 'blob']


class _GitObject(object):
    type = None
    ref = None

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        keys = ('{0}={1}'.format(k, v) for k, v in self.__dict__.viewitems())
        return '<{type}: {int}>'.format(type=self.type, int='; '.join(keys))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Commit(_GitObject):
    type = 'commit'
    author = None
    author_raw = ''
    committer = None
    committer_raw = ''
    tree_ref = ''
    diff = None

    def __init__(self, **kwargs):
        self.parent_refs = []
        super(Commit, self).__init__(**kwargs)


class Tree(_GitObject):
    type = 'tree'
    files = None


class Tag(_GitObject):
    type = 'tag'
    tagger = None
    message = None
    linked_commit = None


class Blob(_GitObject):
    type = 'blob'
    content = None
