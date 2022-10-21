"""EX05 - List Utility Functions."""

__author__ = "730477669."


def only_evens(input1: list[int]) -> list[int]:
    """Displays the even values in the list."""
    new_list: list[int] = []
    i: int = 0

    while i < len(input1):
        if input1[i] % 2 == 0:
            new_list.append(input1[i])
        i += 1
    
    return new_list


def concat(input1: list[int], input2: list[int]) -> list[int]:
    """Combines 2 lists into 1 list."""
    new_list: list[int] = []
    i: int = 0
    j: int = 0

    while i < len(input1) and len(input1) > 0:
        new_list.append(input1[i])
        i += 1
    
    while j < len(input2) and len(input2) > 0:
        new_list.append(input2[j])
        j += 1
    
    return new_list


def sub(input1: list[int], start: int, stop: int) -> list[int]:
    """Displays a portion of the list from start-end."""
    new_list: list[int] = []
    i: int = 0
    
    if start > 0:
        i = start

    if stop > len(input1):
        stop = len(input1)

    while i < stop:
        new_list.append(input1[i])
        i += 1
    
    return new_list