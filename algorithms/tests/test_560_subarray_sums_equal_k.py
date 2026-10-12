from importlib import import_module

import pytest


Solution = import_module("algorithms.560_subarray_sums_equal_k").Solution


@pytest.mark.parametrize(
    ("nums", "k", "expected"),
    [
        pytest.param([1, 1, 1], 2, 2, id="overlapping-subarrays"),
        pytest.param([1, 2, 3], 3, 2, id="different-lengths"),
        pytest.param([5], 5, 1, id="single-match"),
        pytest.param([5], 2, 0, id="single-no-match"),
        pytest.param([0], 0, 1, id="single-zero"),
        pytest.param([1], 0, 0, id="exclude-empty-subarrays"),
        pytest.param([2, 4, 6], 5, 0, id="no-matching-sum"),
        pytest.param([1, 2, 4], 7, 1, id="entire-array"),
        pytest.param([8, 2, 3, 9], 5, 1, id="interior-subarray"),
        pytest.param([1, 4, 2], 3, 0, id="must-be-contiguous"),
        pytest.param([-1, -1, -1], -2, 2, id="negative-target"),
        pytest.param([1, -1, 1, -1], 0, 4, id="repeated-prefix-sums"),
        pytest.param([3, 4, 7, 2, -3, 1, 4, 2], 7, 4, id="mixed-signs"),
        pytest.param([0, 0, 1, 0], 1, 6, id="zeros-around-match"),
        pytest.param([0] * 100, 0, 5050, id="all-zero-subarrays"),
        pytest.param([1000, -1000, 1000], 1000, 3, id="value-boundaries"),
    ],
)
def test_subarray_sum_counts_matching_contiguous_subarrays(nums, k, expected):
    assert Solution().subarraySum(nums, k) == expected

