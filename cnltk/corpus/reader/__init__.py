# Natural Language Toolkit: Corpus Readers
#
# Copyright (C) 2001-2015 NLTK Project
# Author: Steven Bird <stevenbird1@gmail.com>
#         Edward Loper <edloper@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

"""
NLTK corpus readers.  The modules in this package provide functions
that can be used to read corpus fileids in a variety of formats.  These
functions can be used to read both the corpus fileids that are
distributed in the NLTK corpus package, and corpus fileids that are part
of external corpora.

Corpus Reader Functions
=======================
Each corpus module defines one or more "corpus reader functions",
which can be used to read documents from that corpus.  These functions
take an argument, ``item``, which is used to indicate which document
should be read from the corpus:

- If ``item`` is one of the unique identifiers listed in the corpus
  module's ``items`` variable, then the corresponding document will
  be loaded from the NLTK corpus package.
- If ``item`` is a fileid, then that file will be read.

Additionally, corpus reader functions can be given lists of item
names; in which case, they will return a concatenation of the
corresponding documents.

Corpus reader functions are named based on the type of information
they return.  Some common examples, and their return types, are:

- words(): list of str
- sents(): list of (list of str)
- paras(): list of (list of (list of str))
- tagged_words(): list of (str,str) tuple
- tagged_sents(): list of (list of (str,str))
- tagged_paras(): list of (list of (list of (str,str)))
- chunked_sents(): list of (Tree w/ (str,str) leaves)
- parsed_sents(): list of (Tree with str leaves)
- parsed_paras(): list of (list of (Tree with str leaves))
- xml(): A single xml ElementTree
- raw(): unprocessed corpus contents

For example, to read a list of the words in the Brown Corpus, use
``cnltk.corpus.brown.words()``:

    >>> from cnltk.corpus import brown
    >>> print(", ".join(brown.words()))
    The, Fulton, County, Grand, Jury, said, ...

"""

from cnltk.corpus.reader.plaintext import *
from cnltk.corpus.reader.util import *
from cnltk.corpus.reader.api import *
from cnltk.corpus.reader.tagged import *
from cnltk.corpus.reader.cmudict import *
from cnltk.corpus.reader.conll import *
from cnltk.corpus.reader.chunked import *
from cnltk.corpus.reader.wordlist import *
from cnltk.corpus.reader.xmldocs import *
from cnltk.corpus.reader.ppattach import *
from cnltk.corpus.reader.senseval import *
from cnltk.corpus.reader.ieer import *
from cnltk.corpus.reader.sinica_treebank import *
from cnltk.corpus.reader.bracket_parse import *
from cnltk.corpus.reader.indian import *
from cnltk.corpus.reader.toolbox import *
from cnltk.corpus.reader.timit import *
from cnltk.corpus.reader.ycoe import *
from cnltk.corpus.reader.rte import *
from cnltk.corpus.reader.string_category import *
from cnltk.corpus.reader.propbank import *
from cnltk.corpus.reader.verbnet import *
from cnltk.corpus.reader.bnc import *
from cnltk.corpus.reader.nps_chat import *
from cnltk.corpus.reader.wordnet import *
from cnltk.corpus.reader.switchboard import *
from cnltk.corpus.reader.dependency import *
from cnltk.corpus.reader.nombank import *
from cnltk.corpus.reader.ipipan import *
from cnltk.corpus.reader.pl196x import *
from cnltk.corpus.reader.knbc import *
from cnltk.corpus.reader.chasen import *
from cnltk.corpus.reader.childes import *
from cnltk.corpus.reader.aligned import *
from cnltk.corpus.reader.lin import *
from cnltk.corpus.reader.semcor import *
from cnltk.corpus.reader.framenet import *
from cnltk.corpus.reader.udhr import *
from cnltk.corpus.reader.bnc import *
from cnltk.corpus.reader.sentiwordnet import *
from cnltk.corpus.reader.nkjp import *
from cnltk.corpus.reader.crubadan import *

# Make sure that cnltk.corpus.reader.bracket_parse gives the module, not
# the function bracket_parse() defined in cnltk.tree:
from cnltk.corpus.reader import bracket_parse

__all__ = [
    'CorpusReader', 'CategorizedCorpusReader',
    'PlaintextCorpusReader', 'find_corpus_fileids',
    'TaggedCorpusReader', 'CMUDictCorpusReader',
    'ConllChunkCorpusReader', 'WordListCorpusReader',
    'PPAttachmentCorpusReader', 'SensevalCorpusReader',
    'IEERCorpusReader', 'ChunkedCorpusReader',
    'SinicaTreebankCorpusReader', 'BracketParseCorpusReader',
    'IndianCorpusReader', 'ToolboxCorpusReader',
    'TimitCorpusReader', 'YCOECorpusReader',
    'MacMorphoCorpusReader', 'SyntaxCorpusReader',
    'AlpinoCorpusReader', 'RTECorpusReader',
    'StringCategoryCorpusReader','EuroparlCorpusReader',
    'CategorizedBracketParseCorpusReader',
    'CategorizedTaggedCorpusReader',
    'CategorizedPlaintextCorpusReader',
    'PortugueseCategorizedPlaintextCorpusReader',
    'tagged_treebank_para_block_reader',
    'PropbankCorpusReader', 'VerbnetCorpusReader',
    'BNCCorpusReader', 'ConllCorpusReader',
    'XMLCorpusReader', 'NPSChatCorpusReader',
    'SwadeshCorpusReader', 'WordNetCorpusReader',
    'WordNetICCorpusReader', 'SwitchboardCorpusReader',
    'DependencyCorpusReader', 'NombankCorpusReader',
    'IPIPANCorpusReader', 'Pl196xCorpusReader',
    'TEICorpusView', 'KNBCorpusReader', 'ChasenCorpusReader',
    'CHILDESCorpusReader', 'AlignedCorpusReader',
    'TimitTaggedCorpusReader', 'LinThesaurusCorpusReader',
    'SemcorCorpusReader', 'FramenetCorpusReader', 'UdhrCorpusReader',
    'BNCCorpusReader', 'SentiWordNetCorpusReader', 'SentiSynset',
    'NKJPCorpusReader', 'CrubadanCorpusReader'
]
