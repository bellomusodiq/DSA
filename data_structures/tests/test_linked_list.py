import pytest

from data_structures.linked_list import LinkedList


def test_initial_values_are_linked_in_order():
    linked_list = LinkedList(1, 2, 3)

    assert str(linked_list) == "1 -> 2 -> 3"
    assert linked_list.length == 3
    assert linked_list.head.value == 1
    assert linked_list.head.next.value == 2


def test_prepend_adds_value_to_empty_list():
    linked_list = LinkedList()

    linked_list.prepend("first")

    assert str(linked_list) == "first"
    assert linked_list.length == 1


def test_insert_supports_start_middle_and_end_positions():
    linked_list = LinkedList("b", "d")

    linked_list.insert("a", 0)
    linked_list.insert("c", 2)
    linked_list.insert("e")

    assert str(linked_list) == "a -> b -> c -> d -> e"
    assert linked_list.length == 5


def test_delete_removes_head_middle_and_tail():
    linked_list = LinkedList(1, 2, 3, 4)

    linked_list.delete(0)
    linked_list.delete(1)
    linked_list.delete(1)

    assert str(linked_list) == "2"
    assert linked_list.length == 1


@pytest.mark.parametrize("position", [-1, 4])
def test_insert_rejects_out_of_range_position(position):
    linked_list = LinkedList(1, 2, 3)

    with pytest.raises(IndexError, match="insert position is out of range"):
        linked_list.insert(4, position)


@pytest.mark.parametrize("position", [-1, 3])
def test_delete_rejects_out_of_range_position(position):
    linked_list = LinkedList(1, 2, 3)

    with pytest.raises(IndexError, match="delete index is out of range"):
        linked_list.delete(position)
        
@pytest.mark.parametrize("position", [-1, 3])
def test_get_rejects_out_of_range_position(position):
    linked_list = LinkedList(1, 2, 3)

    with pytest.raises(IndexError, match="get index is out of range"):
        linked_list.get(position)
        
def test_get_returns_correct_value():
    linked_list = LinkedList(1, 2, 3)

    assert linked_list.get(0) == 1
    assert linked_list.get(1) == 2
    assert linked_list.get(2) == 3