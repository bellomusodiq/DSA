from importlib import import_module

import pytest

from data_structures.linked_list import LinkedList


Solution = import_module("algorithms.206_reverse_linked_list").Solution


def values_from(head):
    values = []
    while head:
        values.append(head.value)
        head = head.next
    return values


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3], [3, 2, 1]),
        ([1, 2, 3, 4], [4, 3, 2, 1]),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1]),
    ],
)
def test_reversed_list(values, expected):
    linked_list = LinkedList(*values)

    result = Solution().reverseList(linked_list.head)

    assert values_from(result) == expected


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3], [3, 2, 1]),
        ([1, 2, 3, 4], [4, 3, 2, 1]),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1]),
    ],
)
def test_reversed_list_reccurisive(values, expected):
    linked_list = LinkedList(*values)

    result = Solution().reverseList(linked_list.head)

    assert values_from(result) == expected
