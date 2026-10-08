from importlib import import_module

import pytest


Solution = import_module("algorithms.27_remove_element").Solution


@pytest.mark.parametrize(
    ("nums", "val", "expected"),
    [
        pytest.param([], 3, [], id="empty"),
        pytest.param([3], 3, [], id="single-match"),
        pytest.param([2], 3, [2], id="single-non-match"),
        pytest.param([3, 3, 3], 3, [], id="all-match"),
        pytest.param([1, 2, 4], 3, [1, 2, 4], id="no-match"),
        pytest.param([3, 2, 2, 3], 3, [2, 2], id="matches-at-both-ends"),
        pytest.param(
            [0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4], id="mixed"
        ),
        pytest.param([3, 3, 1, 2], 3, [1, 2], id="leading-matches"),
        pytest.param([1, 2, 3, 3], 3, [1, 2], id="trailing-matches"),
        pytest.param([0, 1, 0, 2, 0], 0, [1, 2], id="remove-zero"),
    ],
)
def test_remove_element_returns_count_and_updates_prefix_in_place(nums, val, expected):
    k = Solution().removeElement(nums, val)

    assert type(k) is int
    assert k == len(expected)
    # The retained values may be reordered; values after k are unspecified.
    assert sorted(nums[:k]) == sorted(expected)
