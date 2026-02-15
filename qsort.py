"""
Quicksort implementation with optional key and reverse parameters.
"""

from typing import Any, Callable, Iterable, List, TypeVar

T = TypeVar("T")


def qsort(
    items: Iterable[T], *, key: Callable[[T], Any] | None = None, reverse: bool = False
) -> List[T]:
    """
    Sort the given items using quicksort and return a new list.

    The input iterable is not mutated. Optional key and reverse parameters mirror
    the built-in sorted semantics. Sorting is not guaranteed to be stable.
    """
    arr: List[T] = list(items)
    n = len(arr)
    if n < 2:
        return arr

    key_fn: Callable[[T], Any] = (lambda x: x) if key is None else key
    keys: List[Any] = [key_fn(item) for item in arr]

    stack: List[tuple[int, int]] = [(0, n - 1)]
    while stack:
        low, high = stack.pop()
        if low >= high:
            continue

        pivot = keys[(low + high) // 2]
        i, j = low, high

        while i <= j:
            if not reverse:
                while keys[i] < pivot:
                    i += 1
                while keys[j] > pivot:
                    j -= 1
            else:
                while keys[i] > pivot:
                    i += 1
                while keys[j] < pivot:
                    j -= 1

            if i <= j:
                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    keys[i], keys[j] = keys[j], keys[i]
                i += 1
                j -= 1

        if low < j:
            stack.append((low, j))
        if i < high:
            stack.append((i, high))

    return arr
