from unittest import mock

from moreorless import ask_player_name, \
    DEFAULT_PLAYERNAME_MIN_LENGHT, DEFAULT_PLAYERNAME_MAX_LENGHT

EMPTY_VALUE = ""
ACCEPTED_VALUE = "abcdef"
LESS_VALUE = "adb"
EQUAL_MIN_VALUE = "aded"
EQUAL_MAX_VALUE = "adfzzerartafasdaezrt"
MORE_VALUE = "adadadggergaezhzaferhzegehgzegz"


@mock.patch('builtins.input', side_effect=[EMPTY_VALUE, ACCEPTED_VALUE])
def test_ask_player_name_empty(magic_mock):
    """
    Validate that empty response is doesn t accepted with default configuration
    """
    assert ask_player_name(
        min_lenght=DEFAULT_PLAYERNAME_MIN_LENGHT,
        max_lenght=DEFAULT_PLAYERNAME_MAX_LENGHT) == ACCEPTED_VALUE


@mock.patch('builtins.input', side_effect=[LESS_VALUE, ACCEPTED_VALUE])
def test_ask_player_name_less(magic_mock):
    assert ask_player_name(
        min_lenght=DEFAULT_PLAYERNAME_MIN_LENGHT,
        max_lenght=DEFAULT_PLAYERNAME_MAX_LENGHT) == ACCEPTED_VALUE


@mock.patch('builtins.input', side_effect=[EQUAL_MIN_VALUE, ACCEPTED_VALUE])
def test_ask_player_name_equal_min(magic_mock):
    assert ask_player_name(
        min_lenght=DEFAULT_PLAYERNAME_MIN_LENGHT,
        max_lenght=DEFAULT_PLAYERNAME_MAX_LENGHT) == EQUAL_MIN_VALUE


@mock.patch('builtins.input', side_effect=[ACCEPTED_VALUE])
def test_ask_player_name_valide(magic_mock):
    assert ask_player_name(
        min_lenght=DEFAULT_PLAYERNAME_MIN_LENGHT,
        max_lenght=DEFAULT_PLAYERNAME_MAX_LENGHT) == ACCEPTED_VALUE


@mock.patch('builtins.input', side_effect=[EQUAL_MAX_VALUE, ACCEPTED_VALUE])
def test_ask_player_name_equal_max(magic_mock):
    assert ask_player_name(
        min_lenght=DEFAULT_PLAYERNAME_MIN_LENGHT,
        max_lenght=DEFAULT_PLAYERNAME_MAX_LENGHT) == EQUAL_MAX_VALUE


@mock.patch('builtins.input', side_effect=[MORE_VALUE, ACCEPTED_VALUE])
def test_ask_player_name_more(magic_mock):
    assert ask_player_name(
        min_lenght=DEFAULT_PLAYERNAME_MIN_LENGHT,
        max_lenght=DEFAULT_PLAYERNAME_MAX_LENGHT) == ACCEPTED_VALUE
