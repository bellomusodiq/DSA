from importlib import import_module

import pytest


Solution = import_module("algorithms.75_sort_colors").Solution


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        pytest.param([], [], id="empty"),
        pytest.param([0], [0], id="single-zero"),
        pytest.param([1], [1], id="single-one"),
        pytest.param([2], [2], id="single-two"),
        pytest.param([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2], id="example"),
        pytest.param([2, 0, 1], [0, 1, 2], id="one-of-each"),
        pytest.param([0, 0, 1, 1, 2, 2], [0, 0, 1, 1, 2, 2], id="sorted"),
        pytest.param([2, 2, 1, 1, 0, 0], [0, 0, 1, 1, 2, 2], id="reversed"),
        pytest.param([0, 0, 0], [0, 0, 0], id="all-zeros"),
        pytest.param([1, 1, 1], [1, 1, 1], id="all-ones"),
        pytest.param([2, 2, 2], [2, 2, 2], id="all-twos"),
        pytest.param([2, 1, 2, 1], [1, 1, 2, 2], id="no-zeros"),
        pytest.param([2, 0, 2, 0], [0, 0, 2, 2], id="no-ones"),
        pytest.param([1, 0, 1, 0], [0, 0, 1, 1], id="no-twos"),
        pytest.param([2, 1, 1, 0, 1], [0, 1, 1, 1, 2], id="unequal-counts"),
        pytest.param(
            [2, 1, 0] * 100,
            [0] * 100 + [1] * 100 + [2] * 100,
            id="300-elements",
        ),
    ],
)
def test_sort_colors_sorts_in_place_and_returns_none(nums, expected):
    result = Solution().sortColors(nums)

    assert result is None
    assert nums == expected
