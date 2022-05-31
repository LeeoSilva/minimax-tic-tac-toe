from src.constants import BOARD_ROWS, BOARD_COLS, Player
from random import choice


def get_max_move_count() -> int:
    return BOARD_COLS * BOARD_ROWS


def clear_terminal():
    print("\033c")


def get_random_player():
    players = [Player.X, Player.O]
    return choice(players)


def get_other_player(player: Player) -> Player:
    if player is Player.X:
        return Player.O

    return Player.X
