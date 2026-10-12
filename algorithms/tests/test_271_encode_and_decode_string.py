from importlib import import_module

import pytest


Solution = import_module("algorithms.271_encode_and_decode_string").Solution


CASES = [
    pytest.param([], "", id="empty-list"),
    pytest.param([""], "0#", id="empty-string"),
    pytest.param(["", "", ""], "0#0#0#", id="multiple-empty-strings"),
    pytest.param(["hello"], "5#hello", id="single-string"),
    pytest.param(["lint", "code", "love", "you"],
                 "4#lint4#code4#love3#you", id="example"),
    pytest.param(["", "a", "", "bc", ""], "0#1#a0#2#bc0#",
                 id="interleaved-empty-strings"),
    pytest.param(["#", "##", "3#abc", "0123"], "1##2###5#3#abc4#0123",
                 id="delimiters-and-length-like-content"),
    pytest.param(["same", "same", "different"], "4#same4#same9#different",
                 id="duplicates-and-order"),
    pytest.param([" ", "\t\n", "a\x00b"], "1# 2#\t\n3#a\x00b",
                 id="whitespace-and-null-character"),
    pytest.param(["café", "你好", "🙂", "e\u0301"], "4#café2#你好1#🙂2#e\u0301",
                 id="unicode"),
    pytest.param(["a" * 10, "b" * 100, "end"],
                 "10#" + "a" * 10 + "100#" + "b" * 100 + "3#end",
                 id="multi-digit-lengths"),
]


@pytest.mark.parametrize(("strings", "encoded"), CASES)
def test_encode_uses_length_prefixed_format(strings, encoded):
    assert Solution().encode(strings) == encoded


@pytest.mark.parametrize(("strings", "encoded"), CASES)
def test_decode_restores_strings(strings, encoded):
    assert Solution().decode(encoded) == strings


@pytest.mark.parametrize(("strings", "encoded"), CASES)
def test_round_trip_between_instances(strings, encoded):
    assert Solution().decode(Solution().encode(strings)) == strings
