"""An example of a list utility algorithm."""

# Name: contains
# Function w 2 parameters
# needle- what we'e searching for
# haystack = what we're searching for
# Return type: bool
def contains(needle: str, haystack: list[str]) -> bool:
# Start from first index
    i: int = 0
    # Loop through each index of list
    while i < len(haystack):
#       Test if equal to needle
        if haystack[i] == needle:
#           Yes! Return true
            return True
# Return False
    return False
