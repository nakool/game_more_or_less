#!/usr/bin/env python3.8
"""
Main Executable
"""

import moreorless


SCOREBOARD_PATH = "scoreboard.json"


def main():
    """
    Main Function
    """
    print("Hello World !!")
    moreorless.game(scoreboard_path=SCOREBOARD_PATH)


if __name__ == "__main__":
    main()
