from benchy.api import Benchmark
from benchutil import RelativeBenchmark

nltk_setup= """
import nltk
"""
cnltk_setup= """
import cnltk as nltk
"""
setup="""
from sample import SAMPLE_TEXT
tokenizer = nltk.tokenize.PunktSentenceTokenizer()
"""

statement = "tokenizer.tokenize(SAMPLE_TEXT)"
benchmark1 = Benchmark(statement, nltk_setup+setup, name="nltk")
benchmark2 = Benchmark(statement, cnltk_setup+setup, name="cnltk")

relative_benchmark = RelativeBenchmark(benchmark2, benchmark1, "PunktSentenceTokenizer")

