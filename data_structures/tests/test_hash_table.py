import pytest

from data_structures.hash_table import HashTable


def test_set_get_and_has_key():
    table = HashTable()

    table.set("name", "Ada")

    assert table.get("name") == "Ada"
    assert table.has_key("name") is True
    assert "name" in table
    assert table.len == 1


def test_get_and_has_key_return_missing_results_for_unknown_key():
    table = HashTable()

    assert table.get("missing") is None
    assert table.has_key("missing") is False


def test_collision_keys_are_stored_and_retrieved_independently():
    table = HashTable()

    # Both keys have the same character-code sum and therefore the same hash.
    table.set("ab", 1)
    table.set("ba", 2)

    assert table.get("ab") == 1
    assert table.get("ba") == 2
    assert table.len == 2


def test_updating_a_collision_key_keeps_the_table_length():
    table = HashTable()
    table.set("ab", 1)
    table.set("ba", 2)

    table.set("ba", 20)

    assert table.get("ab") == 1
    assert table.get("ba") == 20
    assert table.len == 2


@pytest.mark.parametrize("key_to_delete", ["ab", "ba"])
def test_delete_removes_only_the_requested_collision_key(key_to_delete):
    table = HashTable()
    table.set("ab", 1)
    table.set("ba", 2)

    table.delete(key_to_delete)

    remaining_key = "ba" if key_to_delete == "ab" else "ab"
    remaining_value = 2 if remaining_key == "ba" else 1
    assert table.get(key_to_delete) is None
    assert table.has_key(key_to_delete) is False
    assert table.get(remaining_key) == remaining_value
    assert table.len == 1


def test_delete_of_missing_key_does_not_change_length():
    table = HashTable([("name", "Ada")])

    table.delete("missing")

    assert table.len == 1
    assert table.get("name") == "Ada"
