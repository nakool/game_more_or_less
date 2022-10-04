from unittest import mock

from moreorless import ask_continue_to_play

VALID_VALUE_INPUT = "Y"
VALID_VALUE_INPUT_LOWER = "y"
VALID_VALUE = True
NOT_VALID_VALUE_INPUT = "n"
NOT_VALID_VALUE = False


@mock.patch('builtins.input', side_effect=[VALID_VALUE_INPUT])
def test_ask_continue_to_play_is_valid(magic_mock):
    """
    Validate if the condition is valid
    """
    assert ask_continue_to_play() == VALID_VALUE


@mock.patch('builtins.input', side_effect=[NOT_VALID_VALUE_INPUT])
def test_ask_continue_to_play_is_not_valid(magic_mock):
    """
    Validate if the condition is not valid
    """
    assert ask_continue_to_play() == NOT_VALID_VALUE


@mock.patch('builtins.input', side_effect=[VALID_VALUE_INPUT_LOWER])
def test_ask_continue_to_play_is_valid_lower(magic_mock):
    """
    Validate if the condition valid lower
    """
    assert ask_continue_to_play() == VALID_VALUE
