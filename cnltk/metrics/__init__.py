# Natural Language Toolkit: Metrics
#
# Copyright (C) 2001-2015 NLTK Project
# Author: Steven Bird <stevenbird1@gmail.com>
#         Edward Loper <edloper@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT
#

"""
NLTK Metrics

Classes and methods for scoring processing modules.
"""

from cnltk.metrics.scores import          (accuracy, precision, recall, f_measure,
                                          log_likelihood, approxrand)
from cnltk.metrics.confusionmatrix import ConfusionMatrix
from cnltk.metrics.distance        import (edit_distance, binary_distance,
                                          jaccard_distance, masi_distance,
                                          interval_distance, custom_distance,
                                          presence, fractional_presence)
from cnltk.metrics.paice           import Paice
from cnltk.metrics.segmentation    import windowdiff, ghd, pk
from cnltk.metrics.agreement       import AnnotationTask
from cnltk.metrics.association     import (NgramAssocMeasures, BigramAssocMeasures,
                                          TrigramAssocMeasures, ContingencyMeasures)
from cnltk.metrics.spearman        import (spearman_correlation, ranks_from_sequence,
                                          ranks_from_scores)
