#!/usr/bin/env python3.8

import random
import json

DEFAULT_MIN_NUMBER = 0
DEFAULT_MAX_NUMBER = 100
DEFAULT_PLAYERNAME_MIN_LENGHT = 4
DEFAULT_PLAYERNAME_MAX_LENGHT = 20


def store_player_score(
        player_name: str,
        player_score: int,
        scoreboard_path: str):
    """ This function is responsible to add the player score to the scoreboard \
    and create it if it don t exist or miss formatted"""
    try:
        with open(scoreboard_path, "r") as _rf:
            _scoreboard = json.load(_rf)
    except FileNotFoundError:
        _scoreboard = list()
    except json.JSONDecodeError:
        print(f"Previous scoreboard at {scoreboard_path=} is miss formatted. \
            We erase it")
        _scoreboard = list()

    _score_entry = {
        "player": player_name,
        "score": player_score
    }
    _scoreboard.append(_score_entry)
    with open(scoreboard_path, "w") as _f:
        json.dump(_scoreboard, _f)


def ask_player_name(
        min_lenght: int = DEFAULT_PLAYERNAME_MIN_LENGHT,
        max_lenght: int = DEFAULT_PLAYERNAME_MAX_LENGHT) -> str:
    _is_valid = False
    while _is_valid is False:
        _player_name = input("Please tell me your name:")
        if len(_player_name) >= min_lenght and len(_player_name) <= max_lenght:
            _is_valid = True
        else:
            print(
                f"This playername is not valid, it need to be between \
                    {min_lenght} and {max_lenght} character!")
    return _player_name


def ask_guess_number(min_guess_number: int, max_guess_number: int) -> int:
    """ Demande une valeur au joueur jusqu a ce qu elle soit comprise entre
    le min_guess_number et le max_guess_number """
    _is_valid = False
    while _is_valid is False:
        try:
            _guess_number = int(input())
        except ValueError:
            print("You don t entered a valid number.")
        else:
            if int(_guess_number) >= min_guess_number and \
                    int(_guess_number) <= max_guess_number:
                _is_valid = True
            else:
                print(
                    f"You have entered the wrong value, \
                        please enter a value between \
                        {min_guess_number} and {max_guess_number}!")
    return _guess_number


def game_init(min_number: int, max_number: int) -> str:
    print("Welcome in more & less game")
    _player = ask_player_name()
    print(
        f"The rules are simple, you have to find \
            the number between {min_number} and {max_number}")
    input("Press enter to play with me.")
    return _player


def ask_continue_to_play() -> bool:
    print("Do you want to play again? [Y/n]")
    if input().upper() == "Y":
        return True
    else:
        print("Thanks you and goodbye")
        return False


def game_turn(
        min_number: int,
        max_number: int,
        scoreboard_path: str,
        player: str) -> bool:
    _enternumber = None
    _guess_number = random.randint(min_number, max_number)
    _try_count = 0

    print(f"Give me a number between {min_number} and {max_number}:")
    while _enternumber != _guess_number:
        _enternumber = ask_guess_number(min_number, max_number)
        # try_count = try_count + 1
        _try_count += 1
        if _enternumber < _guess_number:
            print("it's more.\n")
        elif _enternumber > _guess_number:
            print("It's less.\n")
        elif _enternumber == _guess_number:
            print(f"You're genius {player}!!!")
            print(f"You do it in {_try_count} try")
            store_player_score(
                player_name=player,
                player_score=_try_count,
                scoreboard_path=scoreboard_path)

    return ask_continue_to_play()


def game(
        scoreboard_path: str,
        min_number: int = DEFAULT_MIN_NUMBER,
        max_number: int = DEFAULT_MAX_NUMBER) -> None:
    _player = game_init(min_number, max_number)
    while game_turn(min_number, max_number, scoreboard_path, _player):
        pass

    return None
