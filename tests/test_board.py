import numpy as np
from src.board import Board


def test_initial_state_of_board() -> None:
    board = Board()

    test_board = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"],
    ]

    assert board.state is not None
    assert board.get_state() == test_board


def test_check_primary_diagonal_for_win_x():
    board_state = np.array(
        [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["X", "O", "X"],
        ]
    )

    board = Board(state=board_state)

    board.check_primary_diagonal_for_win()
    assert board.get_winner() == "X"


def test_check_primary_diagonal_for_win_o():
    board_state = np.array(
        [
            ["O", "O", "X"],
            ["X", "O", "X"],
            ["O", "X", "O"],
        ]
    )

    board = Board(state=board_state)

    board.check_primary_diagonal_for_win()
    assert board.get_winner() == "O"


def test_check_primary_diagonal_for_draw():
    board_state = np.array(
        [
            ["O", "O", "X"],
            ["X", "X", "O"],
            ["O", "X", "O"],
        ]
    )

    board = Board(state=board_state)

    board.check_primary_diagonal_for_win()
    assert board.get_winner() == ""


def test_check_secondary_diagonal_for_win_x():
    board_state = np.array(
        [
            ["O", "O", "X"],
            ["O", "X", "X"],
            ["X", "O", "O"],
        ]
    )

    board = Board(state=board_state)

    board.check_secondary_diagonal_for_win()
    assert board.get_winner() == "X"


def test_check_secondary_diagonal_for_win_o():
    board_state = np.array(
        [
            ["X", "X", "O"],
            ["X", "O", "X"],
            ["O", "O", "X"],
        ]
    )

    board = Board(state=board_state)

    board.check_secondary_diagonal_for_win()
    assert board.get_winner() == "O"


def test_check_secondary_diagonal_for_draw():
    board_state = np.array(
        [
            ["X", "X", "O"],
            ["O", "O", "X"],
            ["X", "O", "X"],
        ]
    )

    board = Board(state=board_state)

    board.check_secondary_diagonal_for_win()
    assert board.get_winner() == ""


def test_check_horizontal_for_win_x():
    board_state = np.array(
        [
            ["X", "X", "X"],
            ["X", "O", "X"],
            ["O", "O", "X"],
        ]
    )

    board = Board(state=board_state)

    assert board.check_vertical_for_win() == "X"


def test_check_vertical_for_win_x():
    board_state = np.array(
        [
            ["X", "O", "X"],
            ["X", "O", "X"],
            ["O", "X", "X"],
        ]
    )

    board = Board(state=board_state)

    board.check_vertical_for_win()
    assert board.get_winner() == "X"


def test_check_vertical_for_win_o():
    board_state = np.array(
        [
            ["O", "O", "X"],
            ["O", "X", "O"],
            ["O", "X", "X"],
        ]
    )

    board = Board(state=board_state)

    board.check_vertical_for_win()
    assert board.get_winner() == "O"


def test_check_vertical_for_draw():
    board_state = np.array(
        [
            ["X", "O", "X"],
            ["X", "O", "O"],
            ["O", "X", "X"],
        ]
    )

    board = Board(state=board_state)

    board.check_vertical_for_win()
    assert board.get_winner() == ""


def test_check_horizontal_for_win_x():
    board_state = np.array(
        [
            ["X", "O", "O"],
            ["O", "X", "O"],
            ["X", "X", "X"],
        ]
    )

    board = Board(state=board_state)

    board.check_horizontal_for_win()
    assert board.get_winner() == "X"


def test_check_horizontal_for_win_o():
    board_state = np.array(
        [
            ["X", "O", "X"],
            ["O", "O", "O"],
            ["O", "X", "X"],
        ]
    )

    board = Board(state=board_state)

    board.check_horizontal_for_win()
    assert board.get_winner() == "O"


def test_check_horizontal_for_draw():
    board_state = np.array(
        [
            ["X", "O", "X"],
            ["X", "O", "O"],
            ["O", "X", "X"],
        ]
    )

    board = Board(state=board_state)

    board.check_horizontal_for_win()
    assert board.get_winner() == ""


def test_check_win_x() -> None:
    board_state = np.array(
        [
            ["X", "X", "X"],
            ["O", "O", "X"],
            ["X", "X", "O"],
        ]
    )

    board = Board(state=board_state)

    assert board.check_win() == "X"


def test_check_win_o() -> None:
    board_state = np.array(
        [
            ["X", "O", "X"],
            ["O", "O", "O"],
            ["X", "X", "O"],
        ]
    )

    board = Board(state=board_state)

    assert board.check_win() == "O"
