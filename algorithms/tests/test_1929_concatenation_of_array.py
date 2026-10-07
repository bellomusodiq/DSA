from importlib import import_module

import pytest


Solution = import_module("algorithms.1929_concatenation_of_array").Solution


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([], []),
        ([5], [5, 5]),
        ([1, 2, 1], [1, 2, 1, 1, 2, 1]),
        ([1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1]),
        ([2, 2, 2], [2, 2, 2, 2, 2, 2]),
        ([-1, 0, 2], [-1, 0, 2, -1, 0, 2]),
    ],
)
def test_get_concatenation(nums, expected):
    original = nums.copy()

    result = Solution().getConcatenation(nums)

    assert result == expected
    assert nums == original
    assert result is not nums
