# _*_ coding: utf-8 _*_
# If not specified: Copyright (c) Nikita Kovaliov, maizy.ru, 2013
# See LICENSE.txt for details.
import sys

PY3 = sys.version_info[0] == 3
PY2 = not PY3

if PY3:
    uu = str
else:
    uu = unicode

try:
    from functools import total_ordering
except ImportError:
    def total_ordering(cls):
        """
        Class decorator that fills in missing ordering methods
        http://hg.python.org/cpython/file/529c4defbfd7/Lib/functools.py
        Copyright (C) 2006 Python Software Foundation.
        """
        convert = {
            '__lt__': [('__gt__', lambda self, other: not (self < other or self == other)),
                       ('__le__', lambda self, other: self < other or self == other),
                       ('__ge__', lambda self, other: not self < other)],
            '__le__': [('__ge__', lambda self, other: not self <= other or self == other),
                       ('__lt__', lambda self, other: self <= other and not self == other),
                       ('__gt__', lambda self, other: not self <= other)],
            '__gt__': [('__lt__', lambda self, other: not (self > other or self == other)),
                       ('__ge__', lambda self, other: self > other or self == other),
                       ('__le__', lambda self, other: not self > other)],
            '__ge__': [('__le__', lambda self, other: (not self >= other) or self == other),
                       ('__gt__', lambda self, other: self >= other and not self == other),
                       ('__lt__', lambda self, other: not self >= other)]
        }
        roots = set(dir(cls)) & set(convert)
        if not roots:
            raise ValueError('must define at least one ordering operation: < > <= >=')
        root = max(roots)       # prefer __lt__ to __le__ to __gt__ to __ge__
        for opname, opfunc in convert[root]:
            if opname not in roots:
                opfunc.__name__ = opname
                opfunc.__doc__ = getattr(int, opname).__doc__
                setattr(cls, opname, opfunc)
        return cls


def to_str(cls):
    if hasattr(cls, 'to_str'):
        to_str_func = getattr(cls, 'to_str')
        if PY2:
            setattr(cls, '__unicode__', to_str_func)
        else:
            setattr(cls, '__str__', to_str_func)
    return cls
