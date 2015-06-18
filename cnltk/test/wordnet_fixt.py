# -*- coding: utf-8 -*-
from __future__ import absolute_import

def teardown_module(module=None):
    from cnltk.corpus import wordnet
    wordnet._unload()
