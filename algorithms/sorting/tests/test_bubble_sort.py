from importlib import import_module

import pytest


Solution = import_module("algorithms.sorting.bubble_sort").Solution


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([3, -1, 2, -1, 0, 3], [-1, -1, 0, 2, 3, 3]),
    ],
)
def test_bubble_sort(values, expected):
    result = Solution().bubble_sort(values)

    assert result == expected
    assert result is values
    
@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([3, -1, 2, -1, 0, 3], [-1, -1, 0, 2, 3, 3]),
    ],
)
def test_bubble_sort_recursive(values, expected):
    result = Solution().bubble_sort_recursive(values)

    assert result == expected
    assert result is values
