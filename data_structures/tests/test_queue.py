from data_structures.queue import Queue


def test_enqueue_and_pop_follow_first_in_first_out_order():
    queue = Queue()

    queue.enqueue("first")
    queue.enqueue("second")
    queue.enqueue("third")

    assert queue.peek() == "first"
    assert queue.pop() == "first"
    assert queue.pop() == "second"
    assert queue.pop() == "third"


def test_empty_queue_returns_none_for_pop_and_peek():
    queue = Queue()

    assert queue.can_dequeue is False
    assert queue.peek() is None
    assert queue.pop() is None


def test_pop_of_final_item_resets_linked_list_head_and_tail():
    queue = Queue("only item")

    assert queue.pop() == "only item"
    assert queue.list.length == 0
    assert queue.list.head is None
    assert queue.list.tail is None


def test_enqueue_respects_capacity():
    queue = Queue(capacity=2)

    queue.enqueue("first")
    queue.enqueue("second")
    queue.enqueue("third")

    assert queue.list.length == 2
    assert queue.pop() == "first"
    assert queue.pop() == "second"
