import pytest

from data_structures.max_heap import MaxHeap


@pytest.mark.parametrize(
    "values, expected_peak",
    [
        ([3, 1, 5, 2, 4], 5),
        ([-4, -1, -7], -1),
        ([2, 2, 1], 2),
    ],
)
def test_insert_keeps_largest_value_at_peak(values, expected_peak):
    heap = MaxHeap()

    for value in values:
        heap.insert(value)

    assert heap.peak() == expected_peak
    assert len(heap) == len(values)


def test_pop_returns_values_in_descending_order():
    heap = MaxHeap()
    values = [3, 1, 5, 2, 4]

    for value in values:
        heap.insert(value)

    assert [heap.pop() for _ in values] == [5, 4, 3, 2, 1]
    assert len(heap) == 0


def test_empty_heap_returns_none_for_pop_and_peak():
    heap = MaxHeap()

    assert heap.pop() is None
    assert heap.peak() is None


def test_pop_final_item_empties_heap():
    heap = MaxHeap()
    heap.insert(10)

    assert heap.pop() == 10
    assert len(heap) == 0
    assert heap.peak() is None
