from importlib import import_module

import pytest

from data_structures.linked_list import LinkedList


Solution = import_module("algorithms.143_reorder_linked_list").Solution


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
        ([1, 2], [1, 2]),
        ([1, 2, 3], [1, 3, 2]),
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        ([1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4]),
    ],
)
def test_reorder_list(values, expected):
    linked_list = LinkedList(*values)
    original_head = linked_list.head

    result = Solution().reorderList(linked_list.head)

    assert result is None
    assert linked_list.head is original_head
    assert values_from(linked_list.head) == expected
