# Natural Language Toolkit: Semantic Interpretation
#
# Copyright (C) 2001-2015 NLTK Project
# Author: Ewan Klein <ewan@inf.ed.ac.uk>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

"""
NLTK Semantic Interpretation Package

This package contains classes for representing semantic structure in
formulas of first-order logic and for evaluating such formulas in
set-theoretic models.

    >>> from cnltk.sem import logic
    >>> logic._counter._value = 0

The package has two main components:

 - ``logic`` provides support for analyzing expressions of First
   Order Logic (FOL).
 - ``evaluate`` allows users to recursively determine truth in a
   model for formulas of FOL.

A model consists of a domain of discourse and a valuation function,
which assigns values to non-logical constants. We assume that entities
in the domain are represented as strings such as ``'b1'``, ``'g1'``,
etc. A ``Valuation`` is initialized with a list of (symbol, value)
pairs, where values are entities, sets of entities or sets of tuples
of entities.
The domain of discourse can be inferred from the valuation, and model
is then created with domain and valuation as parameters.

    >>> from cnltk.sem import Valuation, Model
    >>> v = [('adam', 'b1'), ('betty', 'g1'), ('fido', 'd1'),
    ... ('girl', set(['g1', 'g2'])), ('boy', set(['b1', 'b2'])),
    ... ('dog', set(['d1'])),
    ... ('love', set([('b1', 'g1'), ('b2', 'g2'), ('g1', 'b1'), ('g2', 'b1')]))]
    >>> val = Valuation(v)
    >>> dom = val.domain
    >>> m = Model(dom, val)
"""

from cnltk.sem.util import (parse_sents, interpret_sents, evaluate_sents,
                           root_semrep)
from cnltk.sem.evaluate import (Valuation, Assignment, Model, Undefined,
                               is_rel, set2rel, arity, read_valuation)
from cnltk.sem.logic import (boolean_ops, binding_ops, equality_preds,
                           read_logic, Variable, Expression,
                           ApplicationExpression, LogicalExpressionException)
from cnltk.sem.skolemize import skolemize
from cnltk.sem.lfg import FStructure
from cnltk.sem.relextract import (extract_rels, rtuple, clause)
from cnltk.sem.boxer import Boxer
from cnltk.sem.drt import DrtExpression, DRS

# from cnltk.sem.glue import Glue
# from cnltk.sem.hole import HoleSemantics
# from cnltk.sem.cooper_storage import CooperStore

# don't import chat80 as its names are too generic
