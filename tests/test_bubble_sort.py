import os
import sys
import unittest
from dataclasses import dataclass

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from bubble_sort import bubble_sort


@dataclass
class Item:
    value: int
    label: str

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Item):
            return NotImplemented
        return self.value < other.value

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Item):
            return NotImplemented
        return self.value > other.value


class BubbleSortTests(unittest.TestCase):
    def test_empty_list(self) -> None:
        self.assertEqual(bubble_sort([]), [])

    def test_already_sorted(self) -> None:
        items = [1, 2, 3, 4]
        sorted_items = bubble_sort(items)
        self.assertEqual(sorted_items, [1, 2, 3, 4])
        self.assertIsNot(sorted_items, items)
        self.assertEqual(items, [1, 2, 3, 4])

    def test_reverse_sorted(self) -> None:
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicates(self) -> None:
        items = [3, 1, 2, 1, 3]
        self.assertEqual(bubble_sort(items), [1, 1, 2, 3, 3])

    def test_reverse_flag(self) -> None:
        items = [1, 3, 2, 4]
        sorted_items = bubble_sort(items, reverse=True)
        self.assertEqual(sorted_items, [4, 3, 2, 1])
        self.assertEqual(items, [1, 3, 2, 4])

    def test_key_sorting_preserves_stability(self) -> None:
        items = [Item(2, "first"), Item(1, "second"), Item(1, "third")]
        sorted_items = bubble_sort(items, key=lambda item: item.value)
        self.assertEqual([item.value for item in sorted_items], [1, 1, 2])
        self.assertEqual([item.label for item in sorted_items], ["second", "third", "first"])
        self.assertEqual([item.label for item in items], ["first", "second", "third"])

    def test_stability_for_equal_values(self) -> None:
        items = [Item(1, "first"), Item(1, "second"), Item(2, "third")]
        sorted_items = bubble_sort(items)
        self.assertEqual([item.label for item in sorted_items], ["first", "second", "third"])
        self.assertEqual([item.label for item in items], ["first", "second", "third"])


if __name__ == "__main__":
    unittest.main()
