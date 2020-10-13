#!/usr/bin/env python
# coding: utf-8

r"""Benchmark example."""

from ydeos_benchmark.benchmark import benchmark_simple, benchmark_complete, \
    run_benchmark_simple, run_benchmark_complete


def sum_of_squares(x: float, y: float) -> float:
    r"""Sum the squares."""
    return x**2 + y**2


def sum_of_cubes(x: float, y: float) -> float:
    r"""Sum the cubes."""
    return x**3 + y**3


NB_CALLS = 100_000

print("******** Simple benchmarks ********")
func_name, time_ = benchmark_simple(sum_of_squares, [2, 3], {},
                                    n_times=NB_CALLS)
print(f"Function {func_name} called {NB_CALLS} times took {time_} seconds")
func_name, time_ = benchmark_simple(sum_of_cubes, [2, 3], {}, n_times=NB_CALLS)
print(f"Function {func_name} called {NB_CALLS} times took {time_} seconds")

to_profile = ((sum_of_squares, [2, 3], {}), (sum_of_cubes, [2, 3], {}))
run_benchmark_simple(to_profile, n_times=NB_CALLS)

print("******** Complete benchmarks ********")
benchmark_complete(sum_of_squares, [2, 3], {}, n_times=NB_CALLS)
benchmark_complete(sum_of_cubes, [2, 3], {}, n_times=NB_CALLS)

to_profile = ((sum_of_squares, [2, 3], {}), (sum_of_cubes, [2, 3], {}))
run_benchmark_complete(to_profile, n_times=NB_CALLS)
