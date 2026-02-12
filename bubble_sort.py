"""
Bubble sort implementation.
"""

from typing import Any, Callable, Iterable, List, TypeVar

T = TypeVar("T")


def bubble_sort(
    items: Iterable[T], *, key: Callable[[T], Any] | None = None, reverse: bool = False
) -> List[T]:
    """
    Sort the given items using bubble sort and return a new list.

    The input iterable is not mutated. Sorting is stable because equal elements
    are not swapped. Optional key and reverse parameters mirror the built-in
    sorted semantics.
    """
    arr: List[T] = list(items)
    n = len(arr)

    if n < 2:
        return arr

    key_fn: Callable[[T], Any] = (lambda x: x) if key is None else key
    keys: List[Any] = [key_fn(item) for item in arr]

    for end in range(n - 1, 0, -1):
        swapped = False
        for i in range(end):
            should_swap = (
                keys[i] > keys[i + 1] if not reverse else keys[i] < keys[i + 1]
            )
            if should_swap:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                keys[i], keys[i + 1] = keys[i + 1], keys[i]
                swapped = True
        if not swapped:
            break

    return arr
