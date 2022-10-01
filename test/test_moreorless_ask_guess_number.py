from unittest import mock

from moreorless import ask_guess_number, DEFAULT_MIN_NUMBER, DEFAULT_MAX_NUMBER

EMPTY_VALUE = ""
ACCEPTED_VALUE = "48"
LESS_VALUE = "-1"
EQUAL_MIN_VALUE = str(DEFAULT_MIN_NUMBER)
EQUAL_MAX_VALUE = str(DEFAULT_MAX_NUMBER)
MORE_VALUE = "101"
INVALID_VALUE = "***"


@mock.patch('builtins.input', side_effect=[EMPTY_VALUE, ACCEPTED_VALUE])
def test_ask_guess_number_empty(magic_mock):
    assert ask_guess_number(
        min_guess_number=DEFAULT_MIN_NUMBER,
        max_guess_number=DEFAULT_MAX_NUMBER) == int(ACCEPTED_VALUE)


@mock.patch('builtins.input', side_effect=[LESS_VALUE, ACCEPTED_VALUE])
def test_ask_guess_number_less(magic_mock):
    assert ask_guess_number(
        min_guess_number=DEFAULT_MIN_NUMBER,
        max_guess_number=DEFAULT_MAX_NUMBER) == int(ACCEPTED_VALUE)


@mock.patch('builtins.input', side_effect=[EQUAL_MIN_VALUE, ACCEPTED_VALUE])
def test_ask_guess_number_equal_min(magic_mock):
    assert ask_guess_number(
        min_guess_number=DEFAULT_MIN_NUMBER,
        max_guess_number=DEFAULT_MAX_NUMBER) == int(EQUAL_MIN_VALUE)


@mock.patch('builtins.input', side_effect=[ACCEPTED_VALUE])
def test_ask_guess_number_valid(magic_mock):
    assert ask_guess_number(
        min_guess_number=DEFAULT_MIN_NUMBER,
        max_guess_number=DEFAULT_MAX_NUMBER) == int(ACCEPTED_VALUE)


@mock.patch('builtins.input', side_effect=[EQUAL_MAX_VALUE, ACCEPTED_VALUE])
def test_ask_guess_number_equal_max(magic_mock):
    assert ask_guess_number(
        min_guess_number=DEFAULT_MIN_NUMBER,
        max_guess_number=DEFAULT_MAX_NUMBER) == int(EQUAL_MAX_VALUE)


@mock.patch('builtins.input', side_effect=[MORE_VALUE, ACCEPTED_VALUE])
def test_ask_guess_number_more(magic_mock):
    assert ask_guess_number(
        min_guess_number=DEFAULT_MIN_NUMBER,
        max_guess_number=DEFAULT_MAX_NUMBER) == int(ACCEPTED_VALUE)


@mock.patch('builtins.input', side_effect=[INVALID_VALUE, ACCEPTED_VALUE])
def test_ask_guess_number_invalid(magic_mock):
    assert ask_guess_number(
        min_guess_number=DEFAULT_MIN_NUMBER,
        max_guess_number=DEFAULT_MAX_NUMBER) == int(ACCEPTED_VALUE)
