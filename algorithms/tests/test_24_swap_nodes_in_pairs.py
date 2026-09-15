from importlib import import_module

import pytest

from data_structures.linked_list import LinkedList


Solution = import_module("algorithms.24_swap_nodes_in_pairs").Solution


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
        ([1, 2, 3], [2, 1, 3]),
        ([1, 2, 3, 4], [2, 1, 4, 3]),
    ],
)
def test_swap_nodes_in_pairs(values, expected):
    linked_list = LinkedList(*values)

    result = Solution().swapPairs(linked_list.head)

    assert values_from(result) == expected
