from main import fib
from main import fib_iter
from main import fib_gen_ver
from main import FibonacchiLst
import pytest


@pytest.mark.parametrize("n, res", [
    (-1, [0]),
    (0, [0]),
    (1, [0, 1, 1]),
    (5, [0, 1, 1, 2, 3, 5]),
    (10, [0, 1, 1, 2, 3, 5, 8])])
def test_fib_equal(n, res):
    assert fib(n) == res


@pytest.mark.parametrize("l, res", [
    ([1, 1, 1, 1], [1, 1]),
    ([0, 4, 6, 22, 31], [0]),
    ([4, 6, 22, 31], []),
    ([0, 1, 1, 2, 3, 5], [0, 1, 1, 2, 3, 5]),
    ([0, 0, 1, 1, 5, 5, 7, 7], [0, 1, 1, 5])])
def test_fib_iter_equal(l, res):
    assert fib_iter(l) == res


@pytest.mark.parametrize("l, res", [
    ([1, 1, 1, 1], [1, 1]),
    ([0, 4, 6, 22, 31], [0]),
    ([4, 6, 22, 31], []),
    ([0, 1, 1, 2, 3, 5], [0, 1, 1, 2, 3, 5]),
    ([0, 0, 1, 1, 5, 5, 7, 7], [0, 1, 1, 5])])
def test_FibonacchiLst_equal(l, res):
    assert list(FibonacchiLst(l)) == res


@pytest.mark.parametrize("n, res", [
    (-1, [0]),
    (0, [0]),
    (1, [0, 1, 1]),
    (5, [0, 1, 1, 2, 3, 5]),
    (10, [0, 1, 1, 2, 3, 5, 8])])
def test_fib_gen_ver_equal(n, res):
    assert fib_gen_ver(n) == res