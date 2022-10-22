from unittest import mock

from more_or_less import game_init, DEFAULT_MIN_NUMBER, DEFAULT_MAX_NUMBER


VALID_PLAYER_NAME = "player_name"


@mock.patch('builtins.input', side_effect=[""])
@mock.patch('more_or_less.ask_player_name', side_effect=[VALID_PLAYER_NAME])
def test_game_init_is_valid(mock_ask_player_name, mock_input):
    """
    Validate if the condition is valid
    """
    assert game_init(DEFAULT_MIN_NUMBER,
                     DEFAULT_MAX_NUMBER) == VALID_PLAYER_NAME
