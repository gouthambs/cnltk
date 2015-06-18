# Natural Language Toolkit: Parsers
#
# Copyright (C) 2001-2015 NLTK Project
# Author: Steven Bird <stevenbird1@gmail.com>
#         Edward Loper <edloper@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT
#

"""
NLTK Parsers

Classes and interfaces for producing tree structures that represent
the internal organization of a text.  This task is known as "parsing"
the text, and the resulting tree structures are called the text's
"parses".  Typically, the text is a single sentence, and the tree
structure represents the syntactic structure of the sentence.
However, parsers can also be used in other domains.  For example,
parsers can be used to derive the morphological structure of the
morphemes that make up a word, or to derive the discourse structure
for a set of utterances.

Sometimes, a single piece of text can be represented by more than one
tree structure.  Texts represented by more than one tree structure are
called "ambiguous" texts.  Note that there are actually two ways in
which a text can be ambiguous:

    - The text has multiple correct parses.
    - There is not enough information to decide which of several
      candidate parses is correct.

However, the parser module does *not* distinguish these two types of
ambiguity.

The parser module defines ``ParserI``, a standard interface for parsing
texts; and two simple implementations of that interface,
``ShiftReduceParser`` and ``RecursiveDescentParser``.  It also contains
three sub-modules for specialized kinds of parsing:

  - ``cnltk.parser.chart`` defines chart parsing, which uses dynamic
    programming to efficiently parse texts.
  - ``cnltk.parser.probabilistic`` defines probabilistic parsing, which
    associates a probability with each parse.
"""

from cnltk.parse.api import ParserI
from cnltk.parse.chart import (ChartParser, SteppingChartParser, TopDownChartParser,
                              BottomUpChartParser, BottomUpLeftCornerChartParser,
                              LeftCornerChartParser)
from cnltk.parse.featurechart import (FeatureChartParser, FeatureTopDownChartParser,
                                     FeatureBottomUpChartParser,
                                     FeatureBottomUpLeftCornerChartParser)
from cnltk.parse.earleychart import (IncrementalChartParser, EarleyChartParser,
                                    IncrementalTopDownChartParser,
                                    IncrementalBottomUpChartParser,
                                    IncrementalBottomUpLeftCornerChartParser,
                                    IncrementalLeftCornerChartParser,
                                    FeatureIncrementalChartParser,
                                    FeatureEarleyChartParser,
                                    FeatureIncrementalTopDownChartParser,
                                    FeatureIncrementalBottomUpChartParser,
                                    FeatureIncrementalBottomUpLeftCornerChartParser)
from cnltk.parse.pchart import (BottomUpProbabilisticChartParser, InsideChartParser,
                               RandomChartParser, UnsortedChartParser,
                               LongestChartParser)
from cnltk.parse.recursivedescent import (RecursiveDescentParser,
                                         SteppingRecursiveDescentParser)
from cnltk.parse.shiftreduce import (ShiftReduceParser, SteppingShiftReduceParser)
from cnltk.parse.util import load_parser, TestGrammar, extract_test_sentences
from cnltk.parse.viterbi import ViterbiParser
from cnltk.parse.dependencygraph import DependencyGraph
from cnltk.parse.projectivedependencyparser import (ProjectiveDependencyParser,
                                                   ProbabilisticProjectiveDependencyParser)
from cnltk.parse.nonprojectivedependencyparser import (NonprojectiveDependencyParser,
                                                      NaiveBayesDependencyScorer,
                                                      ProbabilisticNonprojectiveParser)
from cnltk.parse.malt import MaltParser
from cnltk.parse.evaluate import DependencyEvaluator
from cnltk.parse.transitionparser import TransitionParser
from cnltk.parse.bllip import BllipParser
