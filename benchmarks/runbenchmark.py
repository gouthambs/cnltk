from benchutil import RelativeBenchmark, BenchmarkRunner
import sys
import os
import glob

CURR_PATH = os.path.abspath(os.path.dirname(__file__))
BASE_PATH= os.path.join(CURR_PATH, "..")
sys.path.append(BASE_PATH)


benchmark_files = glob.glob(os.path.join(CURR_PATH, "bench_*.py"))
modules = [os.path.basename(p).split(".")[0] for p in benchmark_files]
print benchmark_files, modules

by_module = {}
benchmarks = []

for modname in modules:
    ref = __import__(modname)
    by_module[modname] = [v for v in ref.__dict__.values()
                          if isinstance(v, RelativeBenchmark)]
    benchmarks.extend(by_module[modname])
    del sys.modules[modname]


benchmark_runner = BenchmarkRunner(benchmarks)
benchmark_runner.run()

for k, v in benchmark_runner.results.iteritems():
    print k, v["relative"]

