from importlib import import_module

import pytest

from data_structures.linked_list import LinkedList


Solution = import_module("algorithms.19_remove_nth_node_from_end_of_linked_list").Solution


def values_from(head):
    values = []
    while head:
        values.append(head.value)
        head = head.next
    return values


@pytest.mark.parametrize(
    ("values", "n", "expected"),
    [
        ([1, 2, 3, 4, 5, 6], 2, [1, 2, 3, 4, 6]),
        ([1, 2, 3], 1, [1, 2]),
        ([1, 2, 3], 3, [2, 3]),
        ([1, 2], 2, [2]),
        ([1], 1, []),
    ],
)
def test_remove_nth_node_from_end_of_linked_list(values, n, expected):
    linked_list = LinkedList(*values)

    result = Solution().removeNthFromEnd(linked_list.head, n)

    assert values_from(result) == expected
