from importlib import import_module

import pytest


Solution = import_module("algorithms.367_valid_perfect_square").Solution


@pytest.mark.parametrize(
    ("num", "expected"),
    [
        (1, True),
        (4, True),
        (16, True),
        (808201, True),
        (2, False),
        (14, False),
        (999, False),
    ],
)
def test_is_perfect_square(num, expected):
    assert Solution().is_perfect_square(num) is expected
