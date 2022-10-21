"""EX05 - List Utility Unit Test Functions."""

__author__ = "730477669."

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens_only_evens() -> None:
    """Testing only_evens function with list of only evens."""
    list1: list[int] = [4, 4, 4]
    assert only_evens(list1) == [4, 4, 4]
    

def test_only_evens_single_even() -> None:
    """Testing only_evens function with list of any numbers."""
    list1: list[int] = [1, 2, 3]
    assert only_evens(list1) == [2]


def test_only_evens_many_items() -> None:
    """Testing only_evens function with list of values."""
    list1: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(list1) == [2, 4]


def test_concat_empty_lists() -> None:
    """Testing concat function with empty lists."""
    list1: list[int] = []
    list2: list[int] = []
    assert concat(list1, list2) == []


def test_concat_full_list() -> None:
    """Testing concat function with lists of values."""
    list1: list[int] = [1, 2, 3]
    list2: list[int] = [4, 5, 6]
    assert concat(list1, list2) == [1, 2, 3, 4, 5, 6]


def test_concat_one_empty() -> None:
    """Testing concat function with only 1 full list."""
    list1: list[int] = []
    list2: list[int] = [1, 2, 3]
    assert concat(list1, list2) == [1, 2, 3]


def test_sub_big_stop() -> None:
    """Testing sub function with stop value greater than length of list."""
    list1: list[int] = [1, 2, 3]
    assert sub(list1, 0, 5) == [1, 2, 3]


def test_sub_small_stop() -> None:
    """Testing sub function with start value less than 0."""
    list1: list[int] = [1, 2, 3]
    assert sub(list1, -1, 2) == [1, 2]


def test_sub_normal_stop() -> None:
    """Testing sub function with normal start and stop values."""
    list1: list[int] = [1, 2, 3]
    assert sub(list1, 0, 2) == [1, 2]