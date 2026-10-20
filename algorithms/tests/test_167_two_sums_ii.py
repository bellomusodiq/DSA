from importlib import import_module

import pytest


Solution = import_module("algorithms.167_two_sums_ii").Solution


@pytest.mark.parametrize(
    ("numbers", "target", "expected"),
    [
        pytest.param([2, 7, 11, 15], 9, [1, 2], id="example-one"),
        pytest.param([2, 3, 4], 6, [1, 3], id="example-two"),
        pytest.param([-1, 0], -1, [1, 2], id="negative-and-zero"),
        pytest.param([0, 0], 0, [1, 2], id="duplicate-values"),
        pytest.param([1, 2, 3, 4, 5], 9, [4, 5], id="pair-at-right-end"),
        pytest.param([1, 2, 3, 7, 10], 11, [1, 5], id="pair-at-both-ends"),
        pytest.param([-10, -3, 1, 5, 13], 2, [2, 4], id="mixed-signs"),
        pytest.param([1, 1000000000], 1000000001, [1, 2], id="large-values"),
    ],
)
def test_two_sum_ii_returns_one_based_indices(numbers, target, expected):
    original = numbers.copy()

    result = Solution().twoSum(numbers, target)

    assert result == expected
    assert numbers == original
