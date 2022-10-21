"""EX03 - Structured Wordle."""

__author__ = "730477669."


def all(ints: list[int], number: int) -> bool:
    """Given a list of ints and 1 int, should return bool indicating whether or not all ints in list are the same as given int."""
    i: int = 0

    if len(ints) == 0:
        return False

    while i != len(ints):
        if ints[i] != number:
            return False
        i += 1

    return True


def max(input: list[int]) -> int:
    """Given a list of ints, max returns the largest in the List; If list is empty, max returns a ValueError."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    i: int = 0
    maximum: int = input[i]

    while i != len(input):
        if input[i] > maximum:
            maximum = input[i]
        i += 1
        
    return maximum


def is_equal(input1: list[int], input2: list[int]) -> bool:
    """Given two lists of int values, return True if every element at every index is equal in both."""
    if len(input1) != len(input2):
        return False   
    
    i: int = 0

    while i != len(input1):
        if input1[i] != input2[i]:
            return False
        i += 1
    
    return True