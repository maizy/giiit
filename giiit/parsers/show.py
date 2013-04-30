# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

from giiit.multi_version import uu
from giiit.parsers import WrongOutputError, ParserError
from giiit.parsers.results import Commit, Blob
from giiit.parsers.data import GIT_OBJECTS_TYPES


def format_raw(output, force_blob=False, ref=None):
    """
    `git show --format=raw REF`
    with autodetection tree, tag and commit objects

    ref only used with force_blob=True.
    """
    output = uu(output)
    if output[-1] == '\n':
        output = output[:-1]
    # blog returned as is
    if force_blob:
        return Blob(content=output, ref=ref)

    # autodetect type
    lines = output.split('\n')
    if not lines:
        raise WrongOutputError('First line not exists')
    first_line = lines.pop(0)
    type_ref_parts = first_line.split(' ')
    if len(type_ref_parts) != 2:
        raise WrongOutputError('Wrong first line format')
    type, ref = type_ref_parts
    if type not in GIT_OBJECTS_TYPES:
        raise WrongOutputError('Unknown git object type "{0}"'.format(type))

    # TODO: tree & tag support
    if type != 'commit':
        raise ParserError('only "commit" and "blob" types are supported')

    # parse meta data
    meta = []
    while lines:
        line = lines.pop(0)
        if line == '':
            break
        line_parts = line.split(' ', 1)
        if len(line_parts) != 2:
            raise WrongOutputError('Unable to parse meta line "{0}"'.format(line))
        meta.append(line_parts)

    res = None
    # construct result
    if type == 'commit':
        res = Commit(ref=ref)
        for key, value in meta:
            if key == 'tree':
                res.tree_ref = value
            elif key == 'parent':
                res.parent_refs.append(value)
            elif key in ['author', 'committer']:
                setattr(res, key + '_raw', value)
    # TODO: parse commit message and diff

    return res
