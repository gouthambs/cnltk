# -*- coding: utf-8 -*-
"""
Unit tests for cnltk.compat.
See also nltk/test/compat.doctest.
"""
from __future__ import absolute_import, unicode_literals
import unittest

from cnltk.text import Text
from cnltk.compat import PY3, python_2_unicode_compatible

def setup_module(module):
    from nose import SkipTest
    if PY3:
        raise SkipTest("test_2x_compat is for testing cnltk.compat under Python 2.x")


class TestTextTransliteration(unittest.TestCase):
    txt = Text(["São", "Tomé", "and", "Príncipe"])

    def test_repr(self):
        self.assertEqual(repr(self.txt), br"<Text: S\xe3o Tom\xe9 and Pr\xedncipe...>")

    def test_str(self):
        self.assertEqual(str(self.txt), b"<Text: Sao Tome and Principe...>")

