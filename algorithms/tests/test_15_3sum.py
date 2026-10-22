from importlib import import_module

import pytest


Solution = import_module("algorithms.15_3sum").Solution


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        pytest.param([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]], id="example"),
        pytest.param([], [], id="empty"),
        pytest.param([0, 1], [], id="fewer-than-three-values"),
        pytest.param([1, 2, 3, 4], [], id="no-zero-sum-triplet"),
        pytest.param([0, 0, 0], [[0, 0, 0]], id="all-zeroes"),
        pytest.param([0, 0, 0, 0], [[0, 0, 0]], id="duplicate-zero-triplets"),
        pytest.param([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]], id="duplicate-values"),
        pytest.param([-4, -1, -1, 0, 1, 2], [[-1, -1, 2], [-1, 0, 1]], id="negative-values"),
        pytest.param([-3, -2, -1, 1, 2, 3], [[-3, 1, 2], [-2, -1, 3]], id="multiple-triplets"),
    ],
)
def test_three_sum_returns_unique_zero_sum_triplets(nums, expected):
    result = Solution().threeSum(nums)

    assert result == expected
    assert len(result) == len({tuple(triplet) for triplet in result})
    assert all(sum(triplet) == 0 for triplet in result)
