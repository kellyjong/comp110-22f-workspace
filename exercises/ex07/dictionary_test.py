"""EX07 - Dictionary Unit Test Functions."""

__author__ = "730477669."

from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count


def test_invert_one_key() -> None:
    """Testing the invert function with only 1 key."""
    dict_one: dict[str, str] = {'apple': 'cat'}
    
    assert invert(dict_one) == {'cat': 'apple'}


def test_invert_letters() -> None:
    """Testing the invert function with keys of only 1 letter."""
    dict_letters: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    
    assert invert(dict_letters) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_multi() -> None:
    """Testing the invert function with multiple values."""
    dict_same: dict[str, str] = {'kris': 'jordan', 'michael': 'b. jordan'}
    
    assert invert(dict_same) == {'jordan': 'kris', 'b. jordan': 'michael'}


def test_favorite_color_same() -> None:
    """Testing the favorite color function with all values being the same color."""
    dict_same: dict[str, str] = {"Marc": "yellow", "Ezri": "yellow", "Kris": "yellow"}
    
    assert favorite_color(dict_same) == "yellow"


def test_favorite_color_tie() -> None:
    """Testing the favorite color function where there's a tie between colors."""
    dict_tie: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    
    assert favorite_color(dict_tie) == "blue"


def test_favorite_color_none() -> None:
    """Testing the favorite color function where there's no favorite color."""
    dict_none: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "green"}
    
    assert favorite_color(dict_none) == "There is no favorite color."


def test_count_one() -> None:
    """Testing the count function where there's only 1 occurence of each string."""
    list_one: list[str] = ['a', 'b', 'c']

    assert count(list_one) == {'a': 1, 'b': 1, 'c': 1}


def test_count_multi() -> None:
    """Testing the count function where there's multiple occurences of each string."""
    list_multi: list[str] = ['a', 'a', 'b']

    assert count(list_multi) == {'a': 2, 'b': 1}


def test_count_empty() -> None:
    """Testing the count function where there's an empty list."""
    list_empty: list[str] = []
    
    assert count(list_empty) == {}