from importlib import import_module

import pytest


Solution = import_module("algorithms.338_counting_bits").Solution


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        pytest.param(2, [0, 1, 1], id="example-two"),
        pytest.param(5, [0, 1, 1, 2, 1, 2], id="example-five"),
        pytest.param(0, [0], id="zero"),
        pytest.param(1, [0, 1], id="one"),
    ],
)
def test_count_bits(n, expected):
    assert Solution().countBits(n) == expected
