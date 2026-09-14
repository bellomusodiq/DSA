from importlib import import_module

import pytest

from data_structures.linked_list import LinkedList


Solution = import_module("algorithms.23_merge_k_sorted_linked_lists").Solution


def values_from(head):
    values = []
    while head:
        values.append(head.value)
        head = head.next
    return values


@pytest.mark.parametrize(
    ("lists", "expected"),
    [
        ([], []),
        ([[], []], []),
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
    ],
)
def test_merge_k_sorted_linked_lists(lists, expected):
    linked_lists = [LinkedList(*values) for values in lists]

    result = Solution().mergeKLists([linked_list.head for linked_list in linked_lists])

    assert values_from(result) == expected
