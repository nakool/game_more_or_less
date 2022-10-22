from unittest import mock
import json
from more_or_less import store_player_score


SCOREBOARD_VALID = []
PLAYER_NAME = "PLAYER_NAME"
PLAYER_SCORE = 10
SCOREBOARD_VALID_RESULT = [{"player": PLAYER_NAME, "score": PLAYER_SCORE}]
SCOREBOARD_PATH = "scoreboard.json"


@mock.patch('builtins.open')
@mock.patch('json.load')
@mock.patch('json.dump')
def test_store_player_score_valid(
        mock_json_dump: mock.Mock,
        mock_json_load: mock.Mock,
        mock_open: mock.Mock):
    """
    Scenario: scoreboard file exist and is an empty list, \
    add the score and validate that the object store is good
    """
    mock_file = mock.Mock()
    mock_file.__enter__ = mock.Mock()
    mock_file.__exit__ = mock.Mock(return_value=None)
    mock_open.side_effect = [mock_file, mock_file]
    mock_json_load.side_effect = [SCOREBOARD_VALID]

    store_player_score(
        player_name=PLAYER_NAME,
        player_score=PLAYER_SCORE,
        scoreboard_path=SCOREBOARD_PATH
    )

    mock_open.assert_has_calls(calls=[
        mock.call(SCOREBOARD_PATH, "r"),
        mock.call(SCOREBOARD_PATH, "w")
    ], any_order=False)

    mock_json_load.assert_called_once()
    mock_json_dump.assert_called_once_with(
        SCOREBOARD_VALID_RESULT, mock.ANY)


@mock.patch('builtins.open')
@mock.patch('json.load')
@mock.patch('json.dump')
def test_store_player_score_not_exist(
        mock_json_dump: mock.Mock,
        mock_json_load: mock.Mock,
        mock_open: mock.Mock):
    mock_file = mock.Mock()
    mock_file.__enter__ = mock.Mock()
    mock_file.__exit__ = mock.Mock(return_value=None)
    """
    Scenario: the scoreboard file don't exist and we test that is manage and \
    initialize
    """
    mock_open.side_effect = [FileNotFoundError(), mock_file]

    store_player_score(
        player_name=PLAYER_NAME,
        player_score=PLAYER_SCORE,
        scoreboard_path=SCOREBOARD_PATH
    )

    mock_open.assert_has_calls(calls=[
        mock.call(SCOREBOARD_PATH, "r"),
        mock.call(SCOREBOARD_PATH, "w")
    ], any_order=False)

    mock_json_load.assert_not_called()

    mock_json_dump.assert_called_once_with(
        SCOREBOARD_VALID_RESULT, mock.ANY)


@mock.patch('builtins.open')
@mock.patch('json.load')
@mock.patch('json.dump')
def test_store_player_score_not_valid(
        mock_json_dump: mock.Mock,
        mock_json_load: mock.Mock,
        mock_open: mock.Mock):
    """
    Scenario: Scoreboard file exist but the file is missformated
    """
    mock_file = mock.Mock()
    mock_file.__enter__ = mock.Mock()
    mock_file.__exit__ = mock.Mock(return_value=None)
    mock_open.side_effect = [mock_file, mock_file]
    mock_json_load.side_effect = [json.JSONDecodeError("error", "error", 0)]

    store_player_score(
        player_name=PLAYER_NAME,
        player_score=PLAYER_SCORE,
        scoreboard_path=SCOREBOARD_PATH
    )

    mock_open.assert_has_calls(calls=[
        mock.call(SCOREBOARD_PATH, "r"),
        mock.call(SCOREBOARD_PATH, "w")
    ], any_order=False)

    mock_json_load.assert_called_once()
    mock_json_dump.assert_called_once_with(
        SCOREBOARD_VALID_RESULT, mock.ANY)
