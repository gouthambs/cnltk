from benchy.api import Benchmark
from benchutil import RelativeBenchmark

nltk_setup= """
import nltk
"""
setup="""
from sample import SAMPLE_TEXT
tokens = nltk.word_tokenize(SAMPLE_TEXT)
stemmer = nltk.stem.PorterStemmer()
"""
cnltk_setup= """
import cnltk as nltk
"""

statement = "[stemmer.stem(word) for word in tokens]"
benchmark1 = Benchmark(statement, nltk_setup+setup, name="nltk")
benchmark2 = Benchmark(statement, cnltk_setup+setup, name="cnltk")

relative_benchmark = RelativeBenchmark(benchmark2, benchmark1, "PorterStemmer")
