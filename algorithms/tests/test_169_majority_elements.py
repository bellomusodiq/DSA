from importlib import import_module

import pytest


Solution = import_module("algorithms.169_majority_elements").Solution


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        pytest.param([7], 7, id="single-element"),
        pytest.param([4, 4, 4, 4], 4, id="all-identical"),
        pytest.param([3, 2, 3], 3, id="odd-length"),
        pytest.param([2, 2, 1, 1, 1, 2, 2], 2, id="candidate-changes"),
        pytest.param([5, 1, 5, 2, 5, 5], 5, id="even-length"),
        pytest.param([9, 9, 9, 1, 2], 9, id="majority-at-start"),
        pytest.param([1, 2, 9, 9, 9], 9, id="majority-at-end"),
        pytest.param([0, 1, 0, 2, 0], 0, id="zero-majority"),
        pytest.param([-2, 1, -2, 3, -2], -2, id="negative-majority"),
        pytest.param([6, 1, 6, 2, 6, 3, 6], 6, id="alternating-majority"),
    ],
)
def test_majority_element(nums, expected):
    assert Solution().majorityElement(nums) == expected
