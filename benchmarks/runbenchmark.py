from benchutil import RelativeBenchmark, BenchmarkRunner
import sys
import os
BASE_PATH= os.path.join(os.path.dirname(__file__), "..")
sys.path.append(BASE_PATH)

modules=["stem"]
by_module = {}
benchmarks = []

for modname in modules:
    ref = __import__(modname)
    by_module[modname] = [v for v in ref.__dict__.values()
                          if isinstance(v, RelativeBenchmark)]
    benchmarks.extend(by_module[modname])


benchmark_runner = BenchmarkRunner(benchmarks)
benchmark_runner.run()

for k, v in benchmark_runner.results.iteritems():
    print k, v["relative"]

