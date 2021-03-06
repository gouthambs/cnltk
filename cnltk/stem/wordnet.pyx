# Natural Language Toolkit: WordNet stemmer interface
#
# Copyright (C) 2001-2015 NLTK Project
# Author: Steven Bird <stevenbird1@gmail.com>
#         Edward Loper <edloper@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT
from __future__ import unicode_literals

from cnltk.corpus.reader.wordnet import NOUN
from cnltk.corpus import wordnet
from cnltk.compat import python_2_unicode_compatible

@python_2_unicode_compatible
class WordNetLemmatizer(object):
    """
    WordNet Lemmatizer

    Lemmatize using WordNet's built-in morphy function.
    Returns the input word unchanged if it cannot be found in WordNet.

        >>> from cnltk.stem import WordNetLemmatizer
        >>> wnl = WordNetLemmatizer()
        >>> print(wnl.lemmatize('dogs'))
        dog
        >>> print(wnl.lemmatize('churches'))
        church
        >>> print(wnl.lemmatize('aardwolves'))
        aardwolf
        >>> print(wnl.lemmatize('abaci'))
        abacus
        >>> print(wnl.lemmatize('hardrock'))
        hardrock
    """

    def __init__(self):
        pass

    def lemmatize(self, word, pos=NOUN):
        lemmas = wordnet._morphy(word, pos)
        return min(lemmas, key=len) if lemmas else word

    def __repr__(self):
        return '<WordNetLemmatizer>'


# unload wordnet
def teardown_module(module=None):
    from cnltk.corpus import wordnet
    wordnet._unload()

if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
