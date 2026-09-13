from importlib import import_module

import pytest

from data_structures.linked_list import LinkedList


Solution = import_module("algorithms.203_remove_linked_list_elements").Solution


def values_from(head):
    values = []
    while head:
        values.append(head.value)
        head = head.next
    return values


@pytest.mark.parametrize(
    ("values", "value", "expected"),
    [
        ([], 1, []),
        ([1] , 1, []),
        ([2], 1, [2]),
        ([1, 2, 3, 4, 5], 3, [1, 2, 4, 5]),
        ([1, 2, 3, 4, 5], 6, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 3, 5, 3, 6], 3, [1, 2, 4, 5, 6])
    ],
)
def test_remove_list_elements(values, value, expected):
    linked_list = LinkedList(*values)

    result = Solution().removeElements(linked_list.head, value)

    assert values_from(result) == expected
