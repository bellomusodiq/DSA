from importlib import import_module

import pytest


Solution = import_module("algorithms.217_contains_duplicate").Solution


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([], False),
        ([5], False),
        ([1, 2, 3, 4], False),
        ([1, 2, 3, 1], True),
        ([2, 2], True),
        ([7, 7, 7, 7], True),
        ([1, 2, 2, 3], True),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([-3, -1, 0, 2], False),
        ([-1, 0, 2, -1], True),
        ([0, 1, 0], True),
    ],
)
def test_contains_duplicate(nums, expected):
    assert Solution().containsDuplicate(nums) is expected


def test_contains_duplicate_does_not_retain_values_between_calls():
    solution = Solution()

    assert solution.containsDuplicate([1, 2, 1]) is True
    assert solution.containsDuplicate([1, 2, 3]) is False
