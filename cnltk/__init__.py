# Natural Language Toolkit (NLTK)
#
# Copyright (C) 2001-2015 NLTK Project
# Authors: Steven Bird <stevenbird1@gmail.com>
#          Edward Loper <edloper@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

"""
The Natural Language Toolkit (NLTK) is an open source Python library
for Natural Language Processing.  A free online book is available.
(If you use the library for academic research, please cite the book.)

Steven Bird, Ewan Klein, and Edward Loper (2009).
Natural Language Processing with Python.  O'Reilly Media Inc.
http://nltk.org/book
"""
from __future__ import print_function, absolute_import

import os

##//////////////////////////////////////////////////////
##  Metadata
##//////////////////////////////////////////////////////

# Version.  For each new release, the version number should be updated
# in the file VERSION.
try:
    # If a VERSION file exists, use it!
    version_file = os.path.join(os.path.dirname(__file__), 'VERSION')
    with open(version_file, 'r') as infile:
        __version__ = infile.read().strip()
except NameError:
    __version__ = 'unknown (running code interactively?)'
except IOError as ex:
    __version__ = "unknown (%s)" % ex

if __doc__ is not None: # fix for the ``python -OO``
    __doc__ += '\n@version: ' + __version__


# Copyright notice
__copyright__ = """\
Copyright (C) 2001-2015 NLTK Project.

Distributed and Licensed under the Apache License, Version 2.0,
which is included by reference.
"""

__license__ = "Apache License, Version 2.0"
# Description of the toolkit, keywords, and the project's primary URL.
__longdescr__ = """\
The Natural Language Toolkit (NLTK) is a Python package for
natural language processing.  NLTK requires Python 2.6 or higher."""
__keywords__ = ['NLP', 'CL', 'natural language processing',
                'computational linguistics', 'parsing', 'tagging',
                'tokenizing', 'syntax', 'linguistics', 'language',
                'natural language', 'text analytics']
__url__ = "http://nltk.org/"

# Maintainer, contributors, etc.
__maintainer__ = "Steven Bird, Edward Loper, Ewan Klein"
__maintainer_email__ = "stevenbird1@gmail.com"
__author__ = __maintainer__
__author_email__ = __maintainer_email__

# "Trove" classifiers for Python Package Index.
__classifiers__ = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Information Technology',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Scientific/Engineering :: Human Machine Interfaces',
    'Topic :: Scientific/Engineering :: Information Analysis',
    'Topic :: Text Processing',
    'Topic :: Text Processing :: Filters',
    'Topic :: Text Processing :: General',
    'Topic :: Text Processing :: Indexing',
    'Topic :: Text Processing :: Linguistic',
    ]

from cnltk.internals import config_java

# support numpy from pypy
try:
    import numpypy
except ImportError:
    pass

# Override missing methods on environments where it cannot be used like GAE.
import subprocess
if not hasattr(subprocess, 'PIPE'):
    def _fake_PIPE(*args, **kwargs):
        raise NotImplementedError('subprocess.PIPE is not supported.')
    subprocess.PIPE = _fake_PIPE
if not hasattr(subprocess, 'Popen'):
    def _fake_Popen(*args, **kwargs):
        raise NotImplementedError('subprocess.Popen is not supported.')
    subprocess.Popen = _fake_Popen

###########################################################
# TOP-LEVEL MODULES
###########################################################

# Import top-level functionality into top-level namespace

from cnltk.collocations import *
from cnltk.decorators import decorator, memoize
from cnltk.featstruct import *
from cnltk.grammar import *
from cnltk.probability import *
from cnltk.text import *
from cnltk.tree import *
from cnltk.util import *
from cnltk.jsontags import *

###########################################################
# PACKAGES
###########################################################

from cnltk.align import *
from cnltk.chunk import *
from cnltk.classify import *
from cnltk.inference import *
from cnltk.metrics import *
from cnltk.parse import *
from cnltk.tag import *
from cnltk.tokenize import *
from cnltk.sem import *
from cnltk.stem import *

# Packages which can be lazily imported
# (a) we don't import *
# (b) they're slow to import or have run-time dependencies
#     that can safely fail at run time

from cnltk import lazyimport
app = lazyimport.LazyModule('cnltk.app', locals(), globals())
chat = lazyimport.LazyModule('cnltk.chat', locals(), globals())
corpus = lazyimport.LazyModule('cnltk.corpus', locals(), globals())
draw = lazyimport.LazyModule('cnltk.draw', locals(), globals())
toolbox = lazyimport.LazyModule('cnltk.toolbox', locals(), globals())

# Optional loading

try:
    import numpy
except ImportError:
    pass
else:
    from cnltk import cluster

from cnltk.downloader import download, download_shell
try:
    import tkinter
except ImportError:
    pass
else:
    try:
        from cnltk.downloader import download_gui
    except RuntimeError as e:
        import warnings
        warnings.warn("Corpus downloader GUI not loaded "
                      "(RuntimeError during import: %s)" % str(e))

# explicitly import all top-level modules (ensuring
# they override the same names inadvertently imported
# from a subpackage)

from cnltk import align, ccg, chunk, classify, collocations
from cnltk import data, featstruct, grammar, help, inference, metrics
from cnltk import misc, parse, probability, sem, stem, wsd
from cnltk import tag, tbl, text, tokenize, tree, treetransforms, util

# override any accidentally imported demo
def demo():
    print("To run the demo code for a module, type cnltk.module.demo()")
