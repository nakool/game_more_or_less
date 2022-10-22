from unittest import mock

from more_or_less import game, DEFAULT_MAX_NUMBER, DEFAULT_MIN_NUMBER

SCOREBOARD_PATH = "scoreboard.json"
PLAYER_NAME = "playername"


@mock.patch("more_or_less.game_init", side_effect=[PLAYER_NAME])
@mock.patch("more_or_less.game_turn", side_effect=[False])
def test_game_one_turn(mock_game_turn: mock.Mock, mock_game_init: mock.Mock):
    game(min_number=DEFAULT_MIN_NUMBER, max_number=DEFAULT_MAX_NUMBER,
         scoreboard_path=SCOREBOARD_PATH)

    mock_game_init.assert_called_once_with(
        DEFAULT_MIN_NUMBER, DEFAULT_MAX_NUMBER)

    mock_game_turn.assert_called_once_with(
        DEFAULT_MIN_NUMBER, DEFAULT_MAX_NUMBER, SCOREBOARD_PATH, PLAYER_NAME)


@mock.patch("more_or_less.game_init", side_effect=[PLAYER_NAME])
@mock.patch("more_or_less.game_turn", side_effect=[True, False])
def test_game_multiple_turn(mock_game_turn: mock.Mock,
                            mock_game_init: mock.Mock):
    game(min_number=DEFAULT_MIN_NUMBER, max_number=DEFAULT_MAX_NUMBER,
         scoreboard_path=SCOREBOARD_PATH)

    mock_game_init.assert_called_once_with(
        DEFAULT_MIN_NUMBER, DEFAULT_MAX_NUMBER)

    mock_game_turn.assert_has_calls([
        mock.call(DEFAULT_MIN_NUMBER, DEFAULT_MAX_NUMBER,
                  SCOREBOARD_PATH, PLAYER_NAME),
        mock.call(DEFAULT_MIN_NUMBER, DEFAULT_MAX_NUMBER,
                  SCOREBOARD_PATH, PLAYER_NAME)])
