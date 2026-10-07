from importlib import import_module

import pytest


Solution = import_module("algorithms.1_two_sum").Solution


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3, 4], 7, [2, 3]),
        ([1, 4, 6, 8], 9, [0, 3]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([-3, 4, 3, 90], 0, [0, 2]),
        ([0, 4, 3, 0], 0, [0, 3]),
        ([0, 5], 5, [0, 1]),
        ([5, 0], 5, [0, 1]),
        ([1, 1, 3, 5], 8, [2, 3]),
        ([1_000_000_000, -1_000_000_000], 0, [0, 1]),
    ],
)
def test_two_sum(nums, target, expected):
    original = nums.copy()

    result = Solution().twoSum(nums, target)

    assert result == expected
    assert nums == original


def test_two_sum_does_not_retain_values_between_calls():
    solution = Solution()

    assert solution.twoSum([2, 7], 9) == [0, 1]
    assert solution.twoSum([7, 3, 6], 9) == [1, 2]
