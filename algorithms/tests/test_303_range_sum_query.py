from importlib import import_module

import pytest


Solution = import_module("algorithms.303_range_sum_query").Solution


@pytest.mark.parametrize(
    ("nums", "left", "right", "expected"),
    [
        pytest.param([-2, 0, 3, -5, 2, -1], 0, 2, 1, id="example-prefix"),
        pytest.param([-2, 0, 3, -5, 2, -1], 2, 5, -1, id="example-suffix"),
        pytest.param([-2, 0, 3, -5, 2, -1], 0, 5, -3, id="entire-array"),
        pytest.param([7], 0, 0, 7, id="single-positive"),
        pytest.param([-7], 0, 0, -7, id="single-negative"),
        pytest.param([0], 0, 0, 0, id="single-zero"),
        pytest.param([2, 4, 8, 16], 0, 0, 2, id="first-element"),
        pytest.param([2, 4, 8, 16], 3, 3, 16, id="last-element"),
        pytest.param([2, 4, 8, 16], 2, 2, 8, id="interior-element"),
        pytest.param([2, 4, 8, 16], 1, 2, 12, id="inclusive-interior-range"),
        pytest.param([-1, -2, -3, -4], 1, 3, -9, id="all-negative"),
        pytest.param([0, 0, 0, 0], 1, 3, 0, id="all-zeros"),
        pytest.param([9, 3, -3, 7], 1, 2, 0, id="cancelling-values"),
        pytest.param([5, 5, 5, 5], 1, 3, 15, id="repeated-values"),
        pytest.param([100000] * 10000, 0, 9999, 1000000000, id="large-total"),
    ],
)
def test_sum_range_returns_inclusive_sum(nums, left, right, expected):
    assert Solution(nums).sumRange(left, right) == expected


def test_repeated_queries_on_same_instance():
    solution = Solution([-2, 0, 3, -5, 2, -1])

    for left, right, expected in [
        (0, 2, 1),
        (2, 5, -1),
        (0, 5, -3),
        (3, 3, -5),
        (0, 2, 1),
    ]:
        assert solution.sumRange(left, right) == expected


def test_all_valid_ranges_match_direct_sum():
    nums = [4, -2, 0, 7, -9, 3, 3]
    solution = Solution(nums)

    for left in range(len(nums)):
        for right in range(left, len(nums)):
            assert solution.sumRange(left, right) == sum(nums[left:right + 1])


def test_instances_keep_independent_sums():
    first = Solution([1, 2, 3])
    second = Solution([-4, 5])

    assert first.sumRange(0, 2) == 6
    assert second.sumRange(0, 1) == 1
    assert first.sumRange(1, 2) == 5
