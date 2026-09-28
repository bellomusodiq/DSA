import pytest

from data_structures.binary_search_tree import BinarySearchTree


def test_binary_search_tree_insert():
    nums = [10, 7, 11, 8, 14]
    bst = BinarySearchTree()
    for num in nums:
        bst.insert(num)
        
    assert len(bst) == len(nums)
    
@pytest.mark.parametrize(
    "nums, value, expected",
    [
        ([5, 4, 7, 8], 8, True),
        ([], 4, False),
        ([1, 2, 3, 4, 5], 8, False),
        ([3], 3, True)
    ]
)
def test_binary_search_tree_search(nums, value, expected):
    bst = BinarySearchTree()
    for num in nums:
        bst.insert(num)
        
    assert len(bst) == len(nums)
    assert bst.search(value) == expected