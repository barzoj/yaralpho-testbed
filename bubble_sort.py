"""
Bubble sort implementation.
"""

from typing import Iterable, List, TypeVar

T = TypeVar("T")


def bubble_sort(items: Iterable[T]) -> List[T]:
    """
    Sort the given items using bubble sort and return a new list.

    The input iterable is not mutated. Sorting is stable because equal elements
    are not swapped.
    """
    arr: List[T] = list(items)
    n = len(arr)

    if n < 2:
        return arr

    for end in range(n - 1, 0, -1):
        swapped = False
        for i in range(end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break

    return arr

