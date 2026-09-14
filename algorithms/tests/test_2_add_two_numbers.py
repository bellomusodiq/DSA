from importlib import import_module

import pytest

from data_structures.linked_list import LinkedList


Solution = import_module("algorithms.2_add_two_numbers").Solution


def values_from(head):
    values = []
    while head:
        values.append(head.value)
        head = head.next
    return values


@pytest.mark.parametrize(
    ("l1", "l2", "expected"),
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        ([1, 8], [0], [1, 8]),
        ([5], [5], [0, 1]),
    ],
)
def test_add_two_numbers(l1, l2, expected):
    linked_list1 = LinkedList(*l1)
    linked_list2 = LinkedList(*l2)

    result = Solution().addTwoNumbers(linked_list1.head, linked_list2.head)

    assert values_from(result) == expected
