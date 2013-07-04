# _*_ coding: utf-8 _*_
# Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
from __future__ import unicode_literals, absolute_import

from giiit.multi_version import uu
from giiit.parsers import WrongOutputError
from giiit.models.tree import Entity, STATUS_CODES


def porcelain_z(output):
    """
    `git status --porcelain -z`
    also supports `--ignored` option

    test output: tests/parser/resources/status_z_porcelain.out

    Note that with `--porcelain` option all paths returned
    relative to repositiry root.

    """
    output = uu(output)
    parts = output.split('\0')
    if parts[-1] == '':
        parts = parts[:-1]
    entity_cnt = 1
    entities = []
    while parts:
        part = parts.pop(0)
        if len(part) < 4:
            raise WrongOutputError('Bad status string for entity #{0} "{1}"'.format(entity_cnt, part))
        index_status = part[0]
        work_tree_status = part[1]
        path = part[3:]
        new_path = None
        if index_status == 'R':
            if not parts:
                raise WrongOutputError('No new entity path for entity #{0}'.format(entity_cnt))
            new_path, path = path, parts.pop(0)
        entity_cnt += 1
        entities.append(Entity(work_tree_status=STATUS_CODES.get(work_tree_status),
                               work_tree_status_code=work_tree_status,
                               index_status=STATUS_CODES.get(index_status),
                               index_status_code=index_status,
                               path=path,
                               new_path=new_path))
    return entities
