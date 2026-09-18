from importlib import import_module

import pytest

Solution = import_module("algorithms.704_binary_search").Solution

@pytest.mark.parametrize(
   ( "arr", "target", "result"),
   [
       ([], 10, -1),
       ([5], 5, 0),
       ([5], 1, -1),
       ([1, 3, 5, 7, 9], 1, 0),
       ([1, 3, 5, 7, 9], 9, 4),
       ([1, 3, 5, 7, 9], 5, 2),
       ([-10, -3, 0, 4, 8, 12], -3, 1),
       ([-10, -3, 0, 4, 8, 12], 6, -1),
   ]
)
def test_search(arr, target, result):
    assert Solution().binary_search(arr, target) == result