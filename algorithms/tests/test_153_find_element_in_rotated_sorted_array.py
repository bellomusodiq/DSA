from importlib import import_module

import pytest


Solution = import_module("algorithms.153_find_element_in_rotated_sorted_array").Solution


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        pytest.param([4, 5, 6, 7, 0, 1, 2], 0, 4, id="example-found"),
        pytest.param([4, 5, 6, 7, 0, 1, 2], 3, -1, id="example-missing"),
        pytest.param([1], 1, 0, id="single-found"),
        pytest.param([1], 0, -1, id="single-missing"),
        pytest.param([], 5, -1, id="empty"),
        pytest.param([1, 2, 3, 4, 5], 4, 3, id="unrotated-found"),
        pytest.param([1, 2, 3, 4, 5], 0, -1, id="unrotated-missing"),
        pytest.param([3, 1], 1, 1, id="two-elements-found-after-pivot"),
        pytest.param([3, 1], 3, 0, id="two-elements-found-before-pivot"),
        pytest.param([5, 1, 3], 5, 0, id="target-at-first-index"),
        pytest.param([5, 1, 3], 3, 2, id="target-at-last-index"),
        pytest.param([-9, -7, -5, -10], -10, 3, id="negative-values"),
        pytest.param([6, 7, 1, 2, 3, 4, 5], 6, 0, id="pivot-in-right-half"),
    ],
)
def test_search_rotated_sorted_array(nums, target, expected):
    assert Solution().search(nums, target) == expected
