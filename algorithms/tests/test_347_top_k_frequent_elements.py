from importlib import import_module

import pytest


Solution = import_module("algorithms.347_top_k_frequent_elements").Solution


@pytest.mark.parametrize(
    ("nums", "k", "expected"),
    [
        pytest.param([1], 1, [1], id="single-element"),
        pytest.param([4, 4, 4, 4], 1, [4], id="all-identical"),
        pytest.param([1, 1, 1, 2, 2, 3], 2, [1, 2], id="example"),
        pytest.param([3, 1, 2, 2, 2, 1], 1, [2], id="most-frequent-only"),
        pytest.param([3, 1, 2, 1], 3, [1, 2, 3], id="all-distinct-values"),
        pytest.param([4, 2, 7], 3, [4, 2, 7], id="all-frequencies-one"),
        pytest.param(
            [3, 2, 1, 2, 1], 2, [1, 2], id="tie-within-selected-values"
        ),
        pytest.param(
            [4, 3, 2, 1, 1, 1], 1, [1], id="tie-among-excluded-values"
        ),
        pytest.param(
            [-1, -1, -1, -2, -2, -3], 2, [-1, -2], id="negative-values"
        ),
        pytest.param([0, -1, 0, 2, -1, 0], 2, [0, -1], id="zero-and-mixed-signs"),
        pytest.param(
            [10000, -10000, 10000, -10000, -10000, 0],
            2,
            [-10000, 10000],
            id="value-boundaries",
        ),
        pytest.param(
            [9, 8, 7, 7, 8, 8, 7, 7], 2, [7, 8], id="frequency-not-input-order"
        ),
        pytest.param(
            [1] * 1000 + [2] * 100 + [3] * 10 + [4],
            3,
            [1, 2, 3],
            id="uneven-frequencies",
        ),
    ],
)
def test_top_k_frequent_returns_exactly_k_most_frequent_values(nums, k, expected):
    result = Solution().topKFrequent(nums, k)

    assert len(result) == k
    # The problem allows the selected values to be returned in any order.
    assert set(result) == set(expected)
