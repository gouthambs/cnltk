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
test_data = nltk.corpus.treebank.tagged_sents()[3000:]
train_data = nltk.corpus.treebank.tagged_sents()[:3000]
pos_tagger = nltk.tag.tnt.TnT()
pos_tagger.train(train_data)
tokens = [nltk.word_tokenize(sent) for sent in nltk.sent_tokenize(SAMPLE_TEXT)[:10]]
"""


statement = "[pos_tagger.tag(sent_tokens) for sent_tokens in tokens]"

benchmark1_tnt = Benchmark(statement, nltk_setup+setup, name="nltk")
benchmark2_tnt = Benchmark(statement, cnltk_setup+setup, name="cnltk")
relative_benchmark_poter = RelativeBenchmark(benchmark2_tnt,
                                             benchmark1_tnt,
                                             "TnTtagger")
