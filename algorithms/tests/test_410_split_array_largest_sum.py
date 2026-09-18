from importlib import import_module

import pytest


Solution = import_module("algorithms.410_split_array_largest_sum").Solution


@pytest.mark.parametrize(
    ("nums", "m", "expected"),
    [
        ([7, 2, 5, 10, 8], 2, 18),
        ([1, 2, 3, 4, 5], 2, 9),
        ([1, 4, 4], 3, 4),
        ([2, 3, 1, 2, 4, 3], 5, 4),
        ([1, 2, 3, 4, 5], 1, 15),
    ],
)
def test_split_array(nums, m, expected):
    assert Solution().split_array(nums, m) == expected
