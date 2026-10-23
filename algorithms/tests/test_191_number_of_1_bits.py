from importlib import import_module

import pytest


Solution = import_module("algorithms.191_number_of_1_bits").Solution


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        pytest.param(11, 3, id="example-eleven"),
        pytest.param(128, 1, id="example-one-twenty-eight"),
        pytest.param(0, 0, id="zero"),
        pytest.param(1, 1, id="single-set-bit"),
        pytest.param(0b10101010, 4, id="alternating-bits"),
        pytest.param(0xFFFFFFFF, 32, id="all-32-bits-set"),
        pytest.param(0x80000000, 1, id="highest-32-bit-set"),
    ],
)
def test_hamming_weight(n, expected):
    assert Solution().hammingWeight(n) == expected
