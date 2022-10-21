"""EX07 - Dictionary Functions."""

__author__ = "730477669."


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Invert a keys and values of the given dictionary."""
    result: dict[str, str] = {}
    new_key: str = ""

    for key in dict1:
        new_key = dict1[key]

        if new_key in result:
            raise KeyError("There is more than one value with the same name in the original dictionary.")
        else:
            result[new_key] = key

    return result


def favorite_color(dict1: dict[str, str]) -> str:
    """Given a dictionary of people and their favorite color, return the most common favorite color."""
    new: str = ""
    colors: list[str] = []
    color: list[str] = []

    for name in dict1:
        new = dict1[name]

        if new in colors:
            color.append(new)

        colors.append(new)

    if len(color) > 0:
        return color[0]
        
    else:
        return "There is no favorite color."
    

def count(list1: list[str]) -> dict[str, int]:
    """Given a list of strings, return the number of occurences (values) of each string (key) in the list."""
    result: dict[str, int] = {}
    
    for i in list1:

        if i in result:
            result[i] += 1

        else:
            result[i] = 1
    
    return result
