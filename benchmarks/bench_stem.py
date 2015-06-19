from benchy.api import Benchmark
from benchutil import RelativeBenchmark

nltk_setup= """
import nltk
"""
setup="""
from sample import SAMPLE_TEXT
tokens = nltk.word_tokenize(SAMPLE_TEXT)
"""
cnltk_setup= """
import cnltk as nltk
"""

statement = "[stemmer.stem(word) for word in tokens]"

test_setup="""
stemmer = nltk.stem.PorterStemmer()
"""
benchmark1_porter = Benchmark(statement, nltk_setup+setup+test_setup, name="nltk")
benchmark2_porter = Benchmark(statement, cnltk_setup+setup+test_setup, name="cnltk")
relative_benchmark_poter = RelativeBenchmark(benchmark2_porter,
                                             benchmark1_porter,
                                             "PorterStemmer")


test_setup="""
stemmer = nltk.stem.LancasterStemmer()
"""
benchmark1_lancaster = Benchmark(statement, nltk_setup+setup+test_setup, name="nltk")
benchmark2_lancaster = Benchmark(statement, cnltk_setup+setup+test_setup, name="cnltk")
relative_benchmark_lancaster = RelativeBenchmark(benchmark2_lancaster,
                                                 benchmark1_lancaster,
                                                 "LancasterStemmer")
