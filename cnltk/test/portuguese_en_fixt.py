# -*- coding: utf-8 -*-
from __future__ import absolute_import
from cnltk.compat import PY3

from cnltk.corpus import teardown_module


def setup_module(module):
    from nose import SkipTest

    raise SkipTest("portuguese_en.doctest imports cnltk.examples.pt which doesn't exist!")

    if not PY3:
        raise SkipTest(
            "portuguese_en.doctest was skipped because non-ascii doctests are not supported under Python 2.x"
        )
