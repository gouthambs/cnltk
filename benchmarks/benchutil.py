

class RelativeBenchmark(object):

    def __init__(self, benchmark, benchmark_ref, name):
        self.benchmark = benchmark
        self.benchmark_ref = benchmark_ref
        self.name = name
        self.results = {}

    def run(self):
        brr = self.benchmark_ref.run()
        brr.update(dict(name=self.benchmark_ref.name))
        br = self.benchmark.run()
        br.update(dict(name=self.benchmark.name))
        self.results["benchmark"] = br
        self.results["reference"] = brr
        self.results["relative"] = {}
        self.results["relative"] = dict(
            runtime=brr["runtime"]["timing"]/br["runtime"]["timing"],
            memory=brr["memory"]["usage"]/br["memory"]["usage"]
        )
        return self.results


class BenchmarkRunner(object):
    def __init__(self, benchmarks):
        self.benchmarks = benchmarks
        self.results = {}

    def run(self):
        for b in self.benchmarks:
            self.results[b.name] = b.run()
