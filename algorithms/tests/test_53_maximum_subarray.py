from importlib import import_module

import pytest


Solution = import_module("algorithms.53_maximum_subarray").Solution


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        pytest.param([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6, id="example"),
        pytest.param([1], 1, id="single-positive"),
        pytest.param([-1], -1, id="single-negative"),
        pytest.param([-5, -2, -8], -2, id="all-negative"),
        pytest.param([2, 3, 1], 6, id="all-positive"),
        pytest.param([0, 0, 0], 0, id="all-zeroes"),
        pytest.param([5, -10, 6], 6, id="best-subarray-after-drop"),
        pytest.param([4, -1, 2, 1], 6, id="best-subarray-at-end"),
        pytest.param([-2, 1], 1, id="best-subarray-at-end-after-negative"),
    ],
)
def test_max_sub_array(nums, expected):
    assert Solution().maxSubArray(nums) == expected
