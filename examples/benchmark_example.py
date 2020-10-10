#!/usr/bin/env python
# coding: utf-8

r"""Benchmark example"""

from ydeos_benchmark.benchmark import benchmark_simple, benchmark_complete, \
    run_benchmark_simple, run_benchmark_complete


def f(x, y):
    return x**2 + y**2


def g(x, y):
    return x**3 + y**3


nb_calls = 100_000

print("******** Simple benchmarks ********")
func_name, time_ = benchmark_simple(f, [2, 3], {}, n_times=nb_calls)
print(f"Function {func_name} called {nb_calls} times took {time_} seconds")
func_name, time_ = benchmark_simple(g, [2, 3], {}, n_times=nb_calls)
print(f"Function {func_name} called {nb_calls} times took {time_} seconds")

to_profile = ((f, [2, 3], {}), (g, [2, 3], {}))
run_benchmark_simple(to_profile, n_times=nb_calls)

print("******** Complete benchmarks ********")
benchmark_complete(f, [2, 3], {}, n_times=nb_calls)
benchmark_complete(g, [2, 3], {}, n_times=nb_calls)

to_profile = ((f, [2, 3], {}), (g, [2, 3], {}))
run_benchmark_complete(to_profile, n_times=nb_calls)
