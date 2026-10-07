from importlib import import_module

import pytest


Solution = import_module("algorithms.242_valid_anagram").Solution


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("", "", True),
        ("", "a", False),
        ("a", "", False),
        ("a", "a", True),
        ("a", "z", False),
        ("abc", "abc", True),
        ("ab", "abc", False),
        ("abc", "ab", False),
        ("aabbcc", "cbacba", True),
        ("aab", "abb", False),
        ("aaaa", "aaaa", True),
        ("az", "za", True),
        ("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba", True),
    ],
)
def test_is_anagram(s, t, expected):
    assert Solution().isAnagram(s, t) is expected
