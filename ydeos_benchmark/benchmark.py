# coding: utf-8

r"""Benchmarking utilities"""

from typing import Callable
import time
import cProfile
import io
import pstats


def func_n_times(func: Callable, args: list, kwargs: dict, n_times: int) -> None:
    r"""Run func n times with args and kwargs"""
    for _ in range(n_times):
        func(*args, **kwargs)


def benchmark_simple(func: Callable, args: list, kwargs: dict, n_times: int) -> tuple:
    r"""Simple benchmark : stop - start of a function run n times."""
    start = time.time()
    func_n_times(func, args, kwargs, n_times)
    stop = time.time()
    return func.__name__, stop - start


def benchmark_complete(func: Callable,
                       args: list,
                       kwargs: dict,
                       n_times: int,
                       save_results: bool = False):
    r"""Detailed benchmark of a function run n times"""
    results_name = "benchmark/%s.prof" % func.__name__
    pr = cProfile.Profile()
    pr.enable()
    func_n_times(func, args, kwargs, n_times)
    pr.disable()

    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
    ps.print_stats()

    print(s.getvalue())

    if save_results is True:
        with open(results_name, 'w+') as f:
            f.write(s.getvalue())


def run_benchmark_simple(specs: tuple, n_times: int):
    r"""Run a simple benchmark"""
    results = []
    for spec in specs:
        f = spec[0]
        args = spec[1]
        kwargs = spec[2]
        results.append(benchmark_simple(f, args, kwargs, n_times))

    results.sort(key=lambda x: x[1], reverse=True)

    for f, t in results:
        print("%s : %f s" % (f.ljust(40), t))


def run_benchmark_complete(specs: tuple, n_times: int, save_results: bool = False):
    r"""Run a detailed benchmark"""
    for spec in specs:
        f = spec[0]
        args = spec[1]
        kwargs = spec[2]
        benchmark_complete(f, args, kwargs, n_times, save_results=save_results)
