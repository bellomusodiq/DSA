import pytest

from data_structures.binary_search_tree import BinarySearchTree


def test_binary_search_tree_insert():
    nums = [10, 7, 11, 8, 14]
    bst = BinarySearchTree()
    for num in nums:
        bst.insert(num)
        

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
        
    assert bst.search(value) == expected
    
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([5, 4, 7, 8], [4, 5, 7, 8]),
        ([], []),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([3], [3]),
    ]
)
def test_inorder_traversal(nums, expected):
    bst = BinarySearchTree()
    for num in nums:
        bst.insert(num)
        
    assert bst.inorder() == expected
    
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([5, 4, 7, 8], [5, 4, 7, 8]),
        ([], []),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([3], [3]),
    ]
)
def test_preorder_traversal(nums, expected):
    bst = BinarySearchTree()
    for num in nums:
        bst.insert(num)
        
    assert bst.preorder() == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([5, 4, 7, 8], [4, 8, 7, 5]),
        ([], []),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([3], [3])
    ]
)
def test_postorder_traversal(nums, expected):
    bst = BinarySearchTree()
    for num in nums:
        bst.insert(num)

    assert bst.postorder() == expected


@pytest.mark.parametrize(
    "nums, expected_min, expected_max",
    [
        ([5, 4, 7, 8], 4, 8),
        ([1, 2, 3, 4, 5], 1, 5),
        ([3], 3, 3),
        ([-5, 0, 8, -10, 2], -10, 8),
    ]
)
def test_min_and_max(nums, expected_min, expected_max):
    bst = BinarySearchTree()
    for num in nums:
        bst.insert(num)

    assert bst.min() == expected_min
    assert bst.max() == expected_max


def test_min_and_max_on_empty_tree():
    bst = BinarySearchTree()

    assert bst.min() is None
    assert bst.max() is None


@pytest.mark.parametrize(
    "nums, value, expected",
    [
        ([5, 3, 7], 3, [5, 7]),
        ([5, 3, 7, 6], 7, [3, 5, 6]),
        ([5, 3, 7, 6, 8], 5, [3, 6, 7, 8]),
        ([5], 5, []),
    ],
)
def test_binary_search_tree_delete(nums, value, expected):
    bst = BinarySearchTree()
    for num in nums:
        bst.insert(num)

    bst.delete(value)

    assert bst.inorder() == expected


def test_binary_search_tree_delete_missing_value_does_not_change_tree():
    bst = BinarySearchTree()
    for value in [5, 3, 7]:
        bst.insert(value)

    bst.delete(4)

    assert bst.inorder() == [3, 5, 7]
