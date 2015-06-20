#!/usr/bin/env python
#
# Setup script for the Natural Language Toolkit
#
# Copyright (C) 2001-2015 NLTK Project
# Author: Steven Bird <stevenbird1@gmail.com>
#         Edward Loper <edloper@gmail.com>
#         Ewan Klein <ewan@inf.ed.ac.uk>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

# Work around mbcs bug in distutils.
# http://bugs.python.org/issue10945
import codecs
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
    codecs.register(func)

import os
import glob

# Use the VERSION file to get NLTK version
version_file = os.path.join(os.path.dirname(__file__), 'cnltk', 'VERSION')
with open(version_file) as fh:
    nltk_version = fh.read().strip()


# from https://github.com/cvondrick/pyvision/blob/07604f4445683365c5bee57a2276aebe05c244d4/setup.py
# immediately below is stupid hackery for setuptools to work with Cython
import distutils.extension
from distutils.extension import Extension as _Extension
from setuptools import setup, find_packages
distutils.extension.Extension = _Extension
#distutils.command.build_ext.Extension = _Extension
Extension = _Extension
from Cython.Distutils import build_ext
# end stupid hackery

PROJECT_DIR = os.path.dirname(__file__)
def ext_file(submodule, pyx_file):
    if submodule is "":
        pyx_file = os.path.join(PROJECT_DIR, "cnltk", pyx_file)
    else:
        pyx_file = os.path.join(PROJECT_DIR, "cnltk", submodule, pyx_file)
    return pyx_file

def create_extension(submodule, filename):
    if submodule is "":
        return Extension("cnltk.%s" % (filename),
                     [ext_file(submodule,"%s.pyx" % filename)])
    else:
        return Extension("cnltk.%s.%s" % (submodule, filename),
                     [ext_file(submodule,"%s.pyx" % filename)])

submodules = ["stem", "tokenize", "tag", ""]
extension_files = {}
for s in submodules:
    extension_files[s] = [os.path.basename(p).split(".")[0] for p in
                          glob.glob(os.path.join("cnltk", s, "*.pyx"))]


extensions = [create_extension(module, pyxfile)
               for module, pyxfiles in extension_files.iteritems()
               for pyxfile in pyxfiles]

#extensions = [create_extension("stem", "porter"),
#              create_extension("stem", "lancaster"),
#              create_extension("tokenize", "punkt")]

setup(
    name = "cnltk",
    description = "Natural Language Toolkit",
    version = nltk_version,
    url = "http://nltk.org/",
    cmdclass = {"build_ext": build_ext},
    ext_modules=extensions,
    long_description = """\
The Natural Language Toolkit (NLTK) is a Python package for
natural language processing.  NLTK requires Python 2.6, 2.7, or 3.2+.
Package cnltk is a cythonized nltk with performance improvements""",
    license = "Apache License, Version 2.0",
    keywords = ['NLP', 'CL', 'natural language processing',
                'computational linguistics', 'parsing', 'tagging',
                'tokenizing', 'syntax', 'linguistics', 'language',
                'natural language', 'text analytics'],
    maintainer = "Gouthaman Balaraman",
    maintainer_email = "gouthaman.balaraman@gmail.com",
    author = "Steven Bird",
    author_email = "stevenbird1@gmail.com",
    classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Information Technology',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Scientific/Engineering :: Human Machine Interfaces',
    'Topic :: Scientific/Engineering :: Information Analysis',
    'Topic :: Text Processing',
    'Topic :: Text Processing :: Filters',
    'Topic :: Text Processing :: General',
    'Topic :: Text Processing :: Indexing',
    'Topic :: Text Processing :: Linguistic',
    ],
    package_data = {'nltk': ['test/*.doctest', 'VERSION']},
    packages = find_packages(),
    zip_safe=False, # since normal files will be present too?

    )
