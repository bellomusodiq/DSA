from importlib import import_module

import pytest

from data_structures.linked_list import LinkedList


Solution = import_module("algorithms.234_palindrome_linked_list").Solution


def values_from(head):
    values = []
    while head:
        values.append(head.value)
        head = head.next
    return values


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], False),
        ([1], True),
        ([1, 2], False),
        ([1, 1], True),
        ([1, 2, 1], True),
        ([1, 2, 3, 3, 1], False),
        ((1, 3, 3, 5, 5, 3, 3, 1), True)
    ],
)
def test_palindrome_linked_list(values, expected):
    linked_list = LinkedList(*values)

    result = Solution().isPanlindrome(linked_list.head)

    assert result == expected
