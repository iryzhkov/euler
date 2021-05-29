"""List algorithms
"""

def binary_search(array: list, value: int):
    """Finds the first index such that array[i] >= value.

    Args:
        array: a sorted list of integers.
        value: a value to find in the list.

    Returns:
        The index of the first number that is >= value.
    """
    low = 0
    high = len(array) - 1
    mid = 0
 
    while low <= high:
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if array[mid] < value:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif array[mid] > value:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return mid