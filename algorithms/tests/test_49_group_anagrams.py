from importlib import import_module

import pytest


Solution = import_module("algorithms.49_group_anagrams").Solution


@pytest.mark.parametrize(
    ("words", "expected"),
    [
        ([], []),
        ([""], [[""]]),
        (["eat", "tea", "tan", "ate", "nat", "bat"],
         [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
        (["abc", "bca", "cab", "abc"], [["abc", "bca", "cab", "abc"]]),
        (["a", "b", "c"], [["a"], ["b"], ["c"]]),
        (["ab", "ba", "", "a"], [["ab", "ba"], [""], ["a"]]),
    ],
)
def test_group_anagrams_returns_list_of_groups(words, expected):
    result = Solution().groupAnagrams(words)

    assert sorted(sorted(group) for group in result) == sorted(
        sorted(group) for group in expected
    )
