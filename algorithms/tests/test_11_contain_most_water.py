from importlib import import_module

import pytest


Solution = import_module("algorithms.11_contain_most_water").Solution


@pytest.mark.parametrize(
    ("height", "expected"),
    [
        pytest.param([1, 8, 6, 2, 5, 4, 8, 3, 7], 49, id="example-one"),
        pytest.param([1, 1], 1, id="example-two"),
        pytest.param([], 0, id="empty"),
        pytest.param([5], 0, id="single-line"),
        pytest.param([0, 0], 0, id="zero-height-lines"),
        pytest.param([1, 2, 1], 2, id="short-array"),
        pytest.param([4, 3, 2, 1, 4], 16, id="equal-tall-boundaries"),
        pytest.param([1, 2, 3, 4, 5], 6, id="increasing-heights"),
        pytest.param([5, 4, 3, 2, 1], 6, id="decreasing-heights"),
        pytest.param([2, 3, 10, 5, 7, 8, 9], 36, id="maximum-uses-interior-lines"),
    ],
)
def test_max_area(height, expected):
    assert Solution().maxArea(height) == expected
