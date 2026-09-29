import pytest

from data_structures.min_heap import MinHeap


@pytest.mark.parametrize(
    "values, expected_peak",
    [
        ([3, 1, 5, 2, 4], 1),
        ([-4, -1, -7], -7),
        ([2, 2, 1], 1),
    ],
)
def test_insert_keeps_smallest_value_at_peak(values, expected_peak):
    heap = MinHeap()

    for value in values:
        heap.insert(value)

    assert heap.heap[0] == expected_peak
    assert len(heap.heap) == len(values)


def test_pop_returns_values_in_ascending_order():
    heap = MinHeap()
    values = [3, 1, 5, 2, 4]

    for value in values:
        heap.insert(value)

    assert [heap.pop() for _ in values] == [1, 2, 3, 4, 5]
    assert len(heap.heap) == 0


def test_empty_heap_returns_none_for_pop():
    heap = MinHeap()

    assert heap.pop() is None


def test_pop_final_item_empties_heap():
    heap = MinHeap()
    heap.insert(10)

    assert heap.pop() == 10
    assert len(heap.heap) == 0
