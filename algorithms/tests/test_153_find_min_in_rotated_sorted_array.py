from importlib import import_module

import pytest


Solution = import_module("algorithms.153_find_min_in_rotated_sorted_array").Solution


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        pytest.param([3, 4, 5, 1, 2], 1, id="example-one"),
        pytest.param([4, 5, 6, 7, 0, 1, 2], 0, id="example-two"),
        pytest.param([11, 13, 15, 17], 11, id="not-rotated"),
        pytest.param([1], 1, id="single-element"),
        pytest.param([2, 1], 1, id="two-elements-rotated"),
        pytest.param([1, 2], 1, id="two-elements-not-rotated"),
        pytest.param([2, 3, 1], 1, id="minimum-at-end"),
        pytest.param([3, 1, 2], 1, id="minimum-near-start"),
        pytest.param([-4, -2, 0, -7, -6], -7, id="negative-values"),
        pytest.param([0, 1, 2, 3, 4], 0, id="already-sorted-from-zero"),
    ],
)
def test_find_min(nums, expected):
    assert Solution().findMin(nums) == expected
