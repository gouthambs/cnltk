# Natural Language Toolkit: Inference
#
# Copyright (C) 2001-2015 NLTK Project
# Author: Dan Garrette <dhgarrette@gmail.com>
#         Ewan Klein <ewan@inf.ed.ac.uk>
#
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

"""
Classes and interfaces for theorem proving and model building.
"""

from cnltk.inference.api import ParallelProverBuilder, ParallelProverBuilderCommand
from cnltk.inference.mace import Mace, MaceCommand
from cnltk.inference.prover9 import Prover9, Prover9Command
from cnltk.inference.resolution import ResolutionProver, ResolutionProverCommand
from cnltk.inference.tableau import TableauProver, TableauProverCommand
from cnltk.inference.discourse import (ReadingCommand, CfgReadingCommand,
                       DrtGlueReadingCommand, DiscourseTester)
