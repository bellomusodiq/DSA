from importlib import import_module

import pytest


Solution = import_module("algorithms.14_longest_comom_substring").Solution


@pytest.mark.parametrize(
    ("strs", "expected"),
    [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["single"], "single"),
        (["same", "same", "same"], "same"),
        (["", "abc"], ""),
        (["prefix", "pre"], "pre"),
    ],
)
def test_longest_common_substring(strs, expected):
    assert Solution().longestComonSubstring(strs) == expected
