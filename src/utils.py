from typing import Tuple, List
from src.constants import BOARD_ROWS, BOARD_COLS


def get_max_move_count() -> int:
    return BOARD_COLS * BOARD_ROWS


def convert_list_of_2d_indexes_to_1d_indexes(rows: int, cols: int):
    indexes_1d: list = []

    for index in indexes_2d:
        indexes_1d.append(convert_2d_index_to_1d_index(*index))

    return indexes_1d


def clear_terminal():
    print("\033c")


def convert_2d_index_to_1d_index(x: int, y: int) -> int:
    return x * BOARD_COLS + y


def convert_1d_index_to_2d_index(index) -> list:
    x: int = index // BOARD_ROWS
    y: int = index % BOARD_COLS
    return y, x
