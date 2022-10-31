from unittest import mock

from more_or_less import erase_player_score

INCORRECT_VALUE = "1234"
CORRECT_VALUE = None
SCOREBOARD_PATH = "scoreboard.json"


@mock.patch('os.path.exists')
@mock.patch('os.remove')
def test_erase_player_score(mock_os_remove: mock.Mock,
                            mock_os_path_exists: mock.Mock
                            ):
    """
    Validate that empty response is doesn t accepted with default configuration
    """
    mock_file = mock.Mock()
    mock_file.__enter__ = mock.Mock()
    mock_file.__exit__ = mock.Mock(return_value=None)
    mock_os_path_exists.side_effect = [mock_file, mock_file]
    mock_os_remove.side_effect = [INCORRECT_VALUE]

    erase_player_score(scoreboard_path=SCOREBOARD_PATH)

    mock_os_path_exists.assert_called_once()
    mock_os_remove.assert_called_once()
