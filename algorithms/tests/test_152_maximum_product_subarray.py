from importlib import import_module

import pytest


Solution = import_module("algorithms.152_maximum_product_subarray").Solution


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        pytest.param([2, 3, -2, 4], 6, id="example-one"),
        pytest.param([-2, 0, -1], 0, id="example-two"),
        pytest.param([2, 3, -2, 4, -1], 48, id="negative-pair-extends-product"),
        pytest.param([-2], -2, id="single-negative"),
        pytest.param([0], 0, id="single-zero"),
        pytest.param([3], 3, id="single-positive"),
        pytest.param([-2, -3, -4], 12, id="all-negative-even-length-best"),
        pytest.param([-2, -3, -4, -5], 120, id="all-negative-even-count"),
        pytest.param([-2, -3, -4, -5, -6], 360, id="all-negative-odd-count"),
        pytest.param([0, 2, 0, 3, 4], 12, id="zero-separates-products"),
        pytest.param([-1, -2, -9, -6], 108, id="best-subarray-after-negative-prefix"),
        pytest.param([1, -2, 3, 4], 12, id="positive-product-after-two-negatives"),
    ],
)
def test_max_product(nums, expected):
    assert Solution().maxProduct(nums) == expected
