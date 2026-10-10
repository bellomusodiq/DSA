from importlib import import_module
from random import Random

import pytest


Solution = import_module("algorithms.912_sort_an_array").Solution


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        pytest.param([], [], id="empty"),
        pytest.param([7], [7], id="single-element"),
        pytest.param([2, 1], [1, 2], id="two-elements"),
        pytest.param([5, 2, 3, 1], [1, 2, 3, 5], id="example"),
        pytest.param(
            [5, 1, 1, 2, 0, 0], [0, 0, 1, 1, 2, 5], id="duplicates"
        ),
        pytest.param([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], id="already-sorted"),
        pytest.param([5, 4, 3, 2, 1], [1, 2, 3, 4, 5], id="reverse-sorted"),
        pytest.param([3, 3, 3, 3], [3, 3, 3, 3], id="all-equal"),
        pytest.param([-2, -5, -1, -3], [-5, -3, -2, -1], id="negative-values"),
        pytest.param(
            [3, -1, 0, -1, 2], [-1, -1, 0, 2, 3], id="mixed-signs"
        ),
        pytest.param(
            [50000, -50000, 0, 50000, -50000],
            [-50000, -50000, 0, 50000, 50000],
            id="value-boundaries",
        ),
        pytest.param([1, 4, 2, 5, 3, 6], [1, 2, 3, 4, 5, 6], id="interleaved"),
    ],
)
def test_sort_array(nums, expected):
    assert Solution().sortArray(nums) == expected


def test_sort_array_matches_builtin_for_large_input():
    rng = Random(912)
    nums = [rng.randint(-50000, 50000) for _ in range(50000)]
    expected = sorted(nums)

    assert Solution().sortArray(nums) == expected
