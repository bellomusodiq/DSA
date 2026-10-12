from importlib import import_module

import pytest


Solution = import_module("algorithms.1480_running_sum_of_1d_array").Solution


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        pytest.param([1, 2, 3, 4], [1, 3, 6, 10], id="increasing-values"),
        pytest.param([1, 1, 1, 1, 1], [1, 2, 3, 4, 5], id="repeated-values"),
        pytest.param([3, 1, 2, 10, 1], [3, 4, 6, 16, 17], id="mixed-values"),
        pytest.param([5], [5], id="single-positive"),
        pytest.param([-5], [-5], id="single-negative"),
        pytest.param([0], [0], id="single-zero"),
        pytest.param([0, 0, 0], [0, 0, 0], id="all-zeros"),
        pytest.param([-1, -2, -3], [-1, -3, -6], id="all-negative"),
        pytest.param([2, -5, 4, -1], [2, -3, 1, 0], id="mixed-signs"),
        pytest.param([0, 3, 0, -3, 0], [0, 3, 3, 0, 0], id="interleaved-zeros"),
        pytest.param(
            [1000000, 1000000, -1000000],
            [1000000, 2000000, 1000000],
            id="large-values",
        ),
        pytest.param([1] * 1000, list(range(1, 1001)), id="long-array"),
    ],
)
def test_running_sum_returns_cumulative_totals(nums, expected):
    assert Solution().runningSum(nums) == expected
