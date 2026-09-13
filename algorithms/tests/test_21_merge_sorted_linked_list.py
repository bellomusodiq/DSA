from importlib import import_module

import pytest

from data_structures.linked_list import LinkedList


Solution = import_module("algorithms.21_merge_sorted_linked_list").Solution


def values_from(head):
    values = []
    while head:
        values.append(head.value)
        head = head.next
    return values


@pytest.mark.parametrize(
    ("l1", "l2", "expected"),
    [
        ([], [], []),
        ([1], [], [1]),
        ([], [1, 2], [1, 2]),
        ([1, 2, 3], [1, 4, 5], [1, 1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 6], [1, 1, 2, 3, 4, 5, 6])
    ],
)
def test_merge_sorted_linked_list(l1, l2, expected):
    linked_list1 = LinkedList(*l1)
    linked_list2 = LinkedList(*l2)

    result = Solution().mergeSortedList(linked_list1.head, linked_list2.head)

    assert values_from(result) == expected
