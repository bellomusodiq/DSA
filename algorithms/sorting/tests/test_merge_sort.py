from importlib import import_module

import pytest


Solution = import_module("algorithms.sorting.merge_sort").Solution


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
def test_merge_sort(values, expected):
    assert Solution().merge_sort(values) == expected
