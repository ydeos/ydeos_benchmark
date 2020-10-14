# coding: utf-8

r"""Tests for benchmark.py."""

from ydeos_benchmark.benchmark import func_n_times, benchmark_simple, \
    benchmark_complete, run_benchmark_simple, run_benchmark_complete


def f(a_list):
    r"""Return a list slice."""
    return a_list[:-1]


def g(a_list):
    r"""Modify a list by removing its last element."""
    del a_list[-1]


def test_func_n_times():
    r"""Test func_n_times happy path."""
    the_list = list(range(10))

    func_n_times(f, [the_list], {}, n_times=10)
    assert len(the_list) == 10

    func_n_times(g, [the_list], {}, n_times=10)
    assert not the_list  # the list should be empty


def test_benchmark_simple():
    r"""Simple benchmark happy path"""
    name, time_ = benchmark_simple(f, [[1, 2]], {}, n_times=100)
    assert name == "f"
    assert time_ >= 0


def test_run_benchmark_simple():
    r"""Simple benchmark run happy path"""
    assert run_benchmark_simple(((f, [[1, 2]], {}), ), n_times=100) is None


def test_benchmark_complete():
    r"""Complete benchmark happy path"""
    assert benchmark_complete(f, [[1, 2]], {}, n_times=100) is None


def test_run_benchmark_complete():
    r"""Complete benchmark run happy path"""
    assert run_benchmark_complete(((f, [[1, 2]], {}), ), n_times=100) is None
