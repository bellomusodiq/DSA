from importlib import import_module

import pytest


MyHashSet = import_module("algorithms.705_design_hashset").MyHashSet


@pytest.fixture
def hash_set():
    return MyHashSet()


def test_empty_set_does_not_contain_keys(hash_set):
    for key in (0, 1, 10**6):
        assert hash_set.contains(key) is False


@pytest.mark.parametrize("key", [0, 1, 9999, 10000, 10**6])
def test_add_and_remove_key(hash_set, key):
    hash_set.add(key)
    assert hash_set.contains(key) is True

    hash_set.remove(key)
    assert hash_set.contains(key) is False


def test_example_operation_sequence(hash_set):
    hash_set.add(1)
    hash_set.add(2)
    assert hash_set.contains(1) is True
    assert hash_set.contains(3) is False

    hash_set.add(2)
    assert hash_set.contains(2) is True
    hash_set.remove(2)
    assert hash_set.contains(2) is False
    assert hash_set.contains(1) is True


@pytest.mark.parametrize("key", [7, 10007, 20007])
def test_duplicate_add_requires_only_one_removal(hash_set, key):
    for existing in (7, 10007, 20007):
        hash_set.add(existing)
    hash_set.add(key)
    hash_set.add(key)

    hash_set.remove(key)

    assert hash_set.contains(key) is False
    for other in {7, 10007, 20007} - {key}:
        assert hash_set.contains(other) is True


@pytest.mark.parametrize("removed", [7, 10007, 20007], ids=["head", "middle", "tail"])
def test_removing_colliding_key_preserves_other_keys(hash_set, removed):
    keys = (7, 10007, 20007)
    for key in keys:
        hash_set.add(key)
    for key in keys:
        assert hash_set.contains(key) is True
    assert hash_set.contains(30007) is False

    hash_set.remove(removed)

    for key in keys:
        assert hash_set.contains(key) is (key != removed)


def test_removing_missing_key_is_harmless(hash_set):
    hash_set.remove(7)
    hash_set.add(7)
    hash_set.add(10007)

    hash_set.remove(20007)
    hash_set.remove(8)

    assert hash_set.contains(7) is True
    assert hash_set.contains(10007) is True
    assert hash_set.contains(20007) is False
    assert hash_set.contains(8) is False


def test_key_can_be_added_again_after_repeated_removal(hash_set):
    hash_set.add(7)
    hash_set.remove(7)
    hash_set.remove(7)
    assert hash_set.contains(7) is False

    hash_set.add(7)
    assert hash_set.contains(7) is True


def test_instances_have_independent_contents(hash_set):
    other = MyHashSet()
    hash_set.add(7)
    assert other.contains(7) is False

    other.add(10007)
    assert hash_set.contains(10007) is False
