# -*- coding: utf-8 -*-
# Natural Language Toolkit: Transformation-based learning
#
# Copyright (C) 2001-2015 NLTK Project
# Author: Marcus Uneson <marcus.uneson@gmail.com>
#   based on previous (nltk2) version by
#   Christopher Maloof, Edward Loper, Steven Bird
# URL: <http://nltk.org/>
# For license information, see  LICENSE.TXT

"""
Transformation Based Learning

A general purpose package for Transformation Based Learning,
currently used by cnltk.tag.BrillTagger.
"""

from cnltk.tbl.template import Template
#API: Template(...), Template.expand(...)

from cnltk.tbl.feature import Feature
#API: Feature(...), Feature.expand(...)

from cnltk.tbl.rule import Rule
#API: Rule.format(...), Rule.templatetid

from cnltk.tbl.erroranalysis import error_list

