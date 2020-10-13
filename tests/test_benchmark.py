# coding: utf-8

r"""Tests for benchmark.py."""

from ydeos_benchmark.benchmark import func_n_times


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
    assert len(the_list) == 0
