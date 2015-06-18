# Natural Language Toolkit: Applications package
#
# Copyright (C) 2001-2015 NLTK Project
# Author: Edward Loper <edloper@gmail.com>
#         Steven Bird <stevenbird1@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

"""
Interactive NLTK Applications:

chartparser:  Chart Parser
chunkparser:  Regular-Expression Chunk Parser
collocations: Find collocations in text
concordance:  Part-of-speech concordancer
nemo:         Finding (and Replacing) Nemo regular expression tool
rdparser:     Recursive Descent Parser
srparser:     Shift-Reduce Parser
wordnet:      WordNet Browser
"""


# Import Tkinter-based modules if Tkinter is installed
import cnltk.compat
try:
    import tkinter
except ImportError:
    import warnings
    warnings.warn("cnltk.app package not loaded "
                  "(please install Tkinter library).")
else:
    from cnltk.app.chartparser_app import app as chartparser
    from cnltk.app.chunkparser_app import app as chunkparser
    from cnltk.app.collocations_app import app as collocations
    from cnltk.app.concordance_app import app as concordance
    from cnltk.app.nemo_app import app as nemo
    from cnltk.app.rdparser_app import app as rdparser
    from cnltk.app.srparser_app import app as srparser
    from cnltk.app.wordnet_app import app as wordnet

    try:
        from matplotlib import pylab
    except ImportError:
        import warnings
        warnings.warn("cnltk.app.wordfreq not loaded "
                      "(requires the matplotlib library).")
    else:
        from cnltk.app.wordfreq_app import app as wordfreq

# skip doctests from this package
def setup_module(module):
    from nose import SkipTest
    raise SkipTest("cnltk.app examples are not doctests")
