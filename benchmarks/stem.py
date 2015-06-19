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

porter_bench = RelativeBenchmark(benchmark2, benchmark1, "PorterStemmer")


if __name__ == '__main__':
    import sys
    import os
    BASE_PATH= os.path.join(os.path.dirname(__file__), "..")
    sys.path.append(BASE_PATH)

    for b in suite:
        print b.name, b.run()

