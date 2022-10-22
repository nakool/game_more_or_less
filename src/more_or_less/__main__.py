#!/usr/bin/env python3
"""
Main Executable
"""

import pathlib
import typer
from . import game_scoreboard, game, erase_player_score

app = typer.Typer()
SCOREBOARD_PATH = "scoreboard.json"


@app.command()
def erase_scoreboard(scoreboard_path: pathlib.Path = SCOREBOARD_PATH):
    """
    More or less Erase Scoreboard
    """
    erase_player_score(player_name=str,
                       player_score=int,
                       scoreboard_path=scoreboard_path)


@app.command()
def scoreboard(scoreboard_path: pathlib.Path = SCOREBOARD_PATH):
    """
    More or less Scoreboard
    """
    game_scoreboard(scoreboard_path=scoreboard_path)


@app.command()
def more_or_less_game(scoreboard_path: pathlib.Path = SCOREBOARD_PATH):
    """
    More or less Game
    """
    game(scoreboard_path=scoreboard_path)


if __name__ == "__main__":
    try:
        app()
    except SystemExit:
        pass
