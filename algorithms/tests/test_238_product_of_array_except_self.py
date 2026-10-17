from importlib import import_module

import pytest


Solution = import_module("algorithms.238_product_of_array_execpt_self").Solution


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        pytest.param([], [], id="empty"),
        pytest.param([5], [1], id="single-element"),
        pytest.param([1, 2], [2, 1], id="two-elements"),
        pytest.param([1, 2, 3, 4], [24, 12, 8, 6], id="example"),
        pytest.param([0, 1, 2, 3], [6, 0, 0, 0], id="one-zero"),
        pytest.param([1, 0, 3, 0], [0, 0, 0, 0], id="multiple-zeroes"),
        pytest.param([-1, 2, -3, 4], [-24, 12, -8, 6], id="negative-values"),
        pytest.param([0, -2, 3], [-6, 0, 0], id="zero-and-negative"),
    ],
)
def test_product_except_self(nums, expected):
    original = nums.copy()

    result = Solution().productExceptSelf(nums)

    assert result == expected
    assert nums == original
