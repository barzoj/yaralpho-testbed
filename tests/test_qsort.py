import os
import sys
import unittest
from dataclasses import dataclass

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from qsort import qsort


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


class QuickSortTests(unittest.TestCase):
    def test_empty_list(self) -> None:
        self.assertEqual(qsort([]), [])

    def test_already_sorted(self) -> None:
        items = [1, 2, 3, 4]
        sorted_items = qsort(items)
        self.assertEqual(sorted_items, [1, 2, 3, 4])
        self.assertIsNot(sorted_items, items)
        self.assertEqual(items, [1, 2, 3, 4])

    def test_reverse_sorted(self) -> None:
        self.assertEqual(qsort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_reverse_flag(self) -> None:
        items = [1, 3, 2, 4]
        sorted_items = qsort(items, reverse=True)
        self.assertEqual(sorted_items, [4, 3, 2, 1])
        self.assertEqual(items, [1, 3, 2, 4])

    def test_duplicates(self) -> None:
        items = [3, 1, 2, 1, 3]
        self.assertEqual(qsort(items), [1, 1, 2, 3, 3])
        self.assertEqual(items, [3, 1, 2, 1, 3])

    def test_key_sorting_on_custom_objects(self) -> None:
        items = [Item(2, "first"), Item(1, "second"), Item(3, "third"), Item(1, "fourth")]
        sorted_items = qsort(items, key=lambda item: item.value)
        self.assertEqual([item.value for item in sorted_items], [1, 1, 2, 3])
        self.assertEqual([item.label for item in items], ["first", "second", "third", "fourth"])

    def test_iterable_input_tuple(self) -> None:
        data = (4, 1, 3, 2)
        self.assertEqual(qsort(data), [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
