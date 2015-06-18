# Natural Language Toolkit: graphical representations package
#
# Copyright (C) 2001-2015 NLTK Project
# Author: Edward Loper <edloper@gmail.com>
#         Steven Bird <stevenbird1@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

# Import Tkinter-based modules if Tkinter is installed
import cnltk.compat
try:
    import tkinter
except ImportError:
    import warnings
    warnings.warn("cnltk.draw package not loaded "
                  "(please install Tkinter library).")
else:
    from cnltk.draw.cfg import ProductionList, CFGEditor, CFGDemo
    from cnltk.draw.tree import (TreeSegmentWidget, tree_to_treesegment,
                      TreeWidget, TreeView, draw_trees)
    from cnltk.draw.dispersion import dispersion_plot
    from cnltk.draw.table import Table

# skip doctests from this package
def setup_module(module):
    from nose import SkipTest
    raise SkipTest("cnltk.draw examples are not doctests")
