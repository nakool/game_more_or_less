from unittest import mock

from moreorless import game_turn, DEFAULT_MIN_NUMBER, DEFAULT_MAX_NUMBER
from test_moreorless_store_player_score import PLAYER_NAME, SCOREBOARD_PATH


VALUE_INFERIOR = 40
VALUE_EQUAL = 50
VALUE_SUPERIOR = 70
CONTINUE_VALUE = True
SCOREBOARD_PATH = "scoreboard.json"
PLAYER_NAME = "playername"
PLAYER_SCORE = 3


@mock.patch("moreorless.ask_guess_number",
            side_effect=[VALUE_INFERIOR, VALUE_SUPERIOR, VALUE_EQUAL])
@mock.patch("moreorless.ask_continue_to_play", side_effect=[CONTINUE_VALUE])
@mock.patch("moreorless.store_player_score", side_effect=[None])
@mock.patch("random.randint", side_effect=[VALUE_EQUAL])
def test_game_turn(mock_randint: mock.Mock,
                   mock_store_player_score: mock.Mock,
                   mock_ask_continue_to_play: mock.Mock,
                   mock_ask_guess_number: mock.Mock):
    assert game_turn(min_number=DEFAULT_MIN_NUMBER,
                     max_number=DEFAULT_MAX_NUMBER,
                     scoreboard_path=SCOREBOARD_PATH,
                     player=PLAYER_NAME) == CONTINUE_VALUE

    mock_randint.assert_called_once_with(
        DEFAULT_MIN_NUMBER, DEFAULT_MAX_NUMBER)

    mock_ask_guess_number.assert_has_calls([
        mock.call(DEFAULT_MIN_NUMBER, DEFAULT_MAX_NUMBER),
        mock.call(DEFAULT_MIN_NUMBER, DEFAULT_MAX_NUMBER),
        mock.call(DEFAULT_MIN_NUMBER, DEFAULT_MAX_NUMBER)])

    mock_store_player_score.assert_called_once_with(
        player_name=PLAYER_NAME,
        player_score=PLAYER_SCORE,
        scoreboard_path=SCOREBOARD_PATH
    )

    mock_ask_continue_to_play.assert_called_once()
