from data_structures.stack import Stack


def test_push_and_pop_follow_last_in_first_out_order():
    stack = Stack()

    assert stack.push("first") is True
    assert stack.push("second") is True

    assert stack.peak() == "second"
    assert stack.pop() == "second"
    assert stack.pop() == "first"


def test_empty_stack_cannot_pop():
    stack = Stack()

    assert stack.can_pop is False
    assert stack.pop() is None


def test_push_respects_capacity():
    stack = Stack(capacity=2)

    assert stack.push("first") is True
    assert stack.push("second") is True
    assert stack.push("third") is False
    assert str(stack) == "second -> first"
