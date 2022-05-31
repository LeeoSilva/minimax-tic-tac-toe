import numpy as np
from src.board import Board, Player, Result


def test_initial_state_of_board() -> None:
    board = Board()

    expected_board = np.zeros((3, 3))

    assert board.state is not None
    assert board.get_state() == expected_board.tolist()


def test_check_diagonal_for_win_x():
    board_state = np.array(
        [
            [Player.X, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.X, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.X],
        ]
    )

    board = Board(state=board_state)

    board.check_diagonal()
    assert board.fetch_game_result() == Result.X_WON


def test_check_diagonal_for_win_o():
    board_state = np.array(
        [
            [Player.O, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.O, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.O],
        ]
    )

    board = Board(state=board_state)

    board.check_diagonal()
    assert board.fetch_game_result() == Result.O_WON


def test_check_diagonal_for_no_winner():
    board_state = np.array(
        [
            [Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY],
        ]
    )

    board = Board(state=board_state)

    board.check_diagonal()
    assert board.fetch_game_result() == None


def test_stalemate():
    board_state = np.array(
        [
            [Player.X, Player.O, Player.X],
            [Player.O, Player.X, Player.O],
            [Player.X, Player.O, Player.X],
        ]
    )

    board = Board(state=board_state)
    board.check_stalemate()
    assert board.fetch_game_result() == Result.STALEMATE


def test_check_anti_diagonal_for_win_x():
    board_state = np.array(
        [
            [Player.EMPTY, Player.EMPTY, Player.X],
            [Player.EMPTY, Player.X, Player.EMPTY],
            [Player.X, Player.EMPTY, Player.EMPTY],
        ]
    )

    board = Board(state=board_state)

    board.check_anti_diagonal()
    assert board.fetch_game_result() == Result.X_WON


def test_check_anti_diagonal_for_win_o():
    board_state = np.array(
        [
            [Player.EMPTY, Player.EMPTY, Player.O],
            [Player.EMPTY, Player.O, Player.EMPTY],
            [Player.O, Player.EMPTY, Player.EMPTY],
        ]
    )

    board = Board(state=board_state)

    board.check_anti_diagonal()
    assert board.fetch_game_result() == Result.O_WON


def test_check_anti_diagonal_for_no_winner():
    board_state = np.array(
        [
            [Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY],
        ]
    )

    board = Board(state=board_state)

    board.check_anti_diagonal()
    assert board.fetch_game_result() == None


def test_check_horizontal_for_win_x():
    board_state = np.array(
        [
            [Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.X, Player.X, Player.X],
        ]
    )

    board = Board(state=board_state)
    board.check_horizontal()

    assert board.fetch_game_result() == Result.X_WON


def test_check_horizontal_for_win_o():
    board_state = np.array(
        [
            [Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.O, Player.O, Player.O],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY],
        ]
    )

    board = Board(state=board_state)

    board.check_horizontal()
    assert board.fetch_game_result() == Result.O_WON


def test_check_horizontal_for_no_winner():
    board_state = np.array(
        [
            [Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY],
        ]
    )

    board = Board(state=board_state)

    board.check_horizontal()
    assert board.fetch_game_result() == None


def test_check_vertical_for_win_x():
    board_state = np.array(
        [
            [Player.X, Player.EMPTY, Player.EMPTY],
            [Player.X, Player.EMPTY, Player.EMPTY],
            [Player.X, Player.EMPTY, Player.EMPTY],
        ]
    )

    board = Board(state=board_state)

    board.check_vertical()
    assert board.fetch_game_result() == Result.X_WON


def test_check_vertical_for_win_o():
    board_state = np.array(
        [
            [Player.EMPTY, Player.O, Player.EMPTY],
            [Player.EMPTY, Player.O, Player.EMPTY],
            [Player.EMPTY, Player.O, Player.EMPTY],
        ]
    )

    board = Board(state=board_state)

    board.check_vertical()
    assert board.fetch_game_result() == Result.O_WON


def test_check_vertical_for_no_winner():
    board_state = np.array(
        [
            [Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY],
        ]
    )

    board = Board(state=board_state)

    board.check_vertical()
    assert board.fetch_game_result() == None
    assert board.move_count == 0


def test_check_game_over_x_won() -> None:
    board_state = np.array(
        [
            [Player.X, Player.X, Player.X],
            [Player.O, Player.O, Player.EMPTY],
            [Player.EMPTY, Player.O, Player.X],
        ]
    )

    board = Board(state=board_state)

    assert board.is_game_over() is True
    assert board.move_count == 7
    assert board.fetch_game_result() == Result.X_WON


def test_check_game_over_o_won() -> None:
    board_state = np.array(
        [
            [Player.O, Player.X, Player.X],
            [Player.O, Player.O, Player.X],
            [Player.X, Player.O, Player.O],
        ]
    )

    board = Board(state=board_state)

    assert board.is_game_over() is True
    assert board.fetch_game_result() == Result.O_WON
    assert board.move_count == 9


def test_check_game_over_stalemate() -> None:
    board_state = np.array(
        [
            [Player.X, Player.X, Player.O],
            [Player.O, Player.O, Player.X],
            [Player.X, Player.O, Player.O],
        ]
    )

    board = Board(state=board_state)

    assert board.is_game_over() is True
    assert board.fetch_game_result() == Result.STALEMATE
    assert board.move_count == 9


def test_get_available_moves() -> None:
    board_state = np.array(
        [
            [Player.EMPTY, Player.X, Player.O],
            [Player.O, Player.EMPTY, Player.X],
            [Player.X, Player.O, Player.O],
        ]
    )

    board = Board(state=board_state)

    assert board.get_available_moves() == [0, 4]

    board.make_move(0)

    assert board.get_available_moves() == [4]

    board.make_move(4)

    assert board.get_available_moves() == []


def test_make_move() -> None:
    board = Board()

    board.make_move(2)

    board_state = board.get_state()

    assert board_state[0][2] == Player.X
    assert board.move_count == 1
    assert board.player == Player.O

    assert len(board.move_history) == 1
    assert board.move_history[0] == 2


def test_full_game() -> None:
    """
    Should test this case:

     X  |  X  |  O
    ____|_____|____
        |     |
     O  |  O  |  X
    ____|_____|____
        |     |
     X  |  O  |  X
    """

    board = Board()

    assert board.get_available_moves() == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert board.player == Player.X
    assert board.move_count == 0
    assert board.move_history == []
    assert board.game_result is None

    board.make_move(0)  # X
    assert board.get_available_moves() == [1, 2, 3, 4, 5, 6, 7, 8]
    assert board.player == Player.O
    assert board.move_count == 1
    assert board.move_history == [0]
    assert board.game_result is None

    board.make_move(2)  # O
    assert board.get_available_moves() == [1, 3, 4, 5, 6, 7, 8]
    assert board.player == Player.X
    assert board.move_count == 2
    assert board.move_history == [0, 2]
    assert board.game_result is None

    board.make_move(1)  # X
    assert board.get_available_moves() == [3, 4, 5, 6, 7, 8]
    assert board.player == Player.O
    assert board.move_count == 3
    assert board.move_history == [0, 2, 1]
    assert board.game_result is None

    board.make_move(3)  # O
    assert board.get_available_moves() == [4, 5, 6, 7, 8]
    assert board.player == Player.X
    assert board.move_count == 4
    assert board.move_history == [0, 2, 1, 3]
    assert board.game_result is None

    board.make_move(5)  # X
    assert board.get_available_moves() == [4, 6, 7, 8]
    assert board.player == Player.O
    assert board.move_count == 5
    assert board.move_history == [0, 2, 1, 3, 5]
    assert board.game_result is None

    board.make_move(4)  # O
    assert board.get_available_moves() == [6, 7, 8]
    assert board.player == Player.X
    assert board.move_count == 6
    assert board.move_history == [0, 2, 1, 3, 5, 4]
    assert board.game_result is None

    board.make_move(6)  # X
    assert board.get_available_moves() == [7, 8]
    assert board.player == Player.O
    assert board.move_count == 7
    assert board.move_history == [0, 2, 1, 3, 5, 4, 6]
    assert board.game_result is None

    board.make_move(7)  # O
    assert board.get_available_moves() == [8]
    assert board.player == Player.X
    assert board.move_count == 8
    assert board.move_history == [0, 2, 1, 3, 5, 4, 6, 7]
    assert board.game_result is None

    board.make_move(8)  # X
    assert board.get_available_moves() == []
    assert board.player == Player.O
    assert board.move_count == 9
    assert board.move_history == [0, 2, 1, 3, 5, 4, 6, 7, 8]
    assert board.game_result is Result.STALEMATE

    board_state = board.get_state()

    assert board_state[0][0] == Player.X
    assert board_state[0][1] == Player.X
    assert board_state[0][2] == Player.O
    assert board_state[1][0] == Player.O
    assert board_state[1][1] == Player.O
    assert board_state[1][2] == Player.X
    assert board_state[2][0] == Player.X
    assert board_state[2][1] == Player.O
    assert board_state[2][0] == Player.X

    assert board.move_count == 9
    assert board.fetch_game_result() == Result.STALEMATE
    assert board.player == Player.O

    assert len(board.move_history) == 9


def test_undo_move() -> None:
    """
    Should test this case:

     X  |  X  |  X
    ____|_____|____
        |     |
        |  O  |
    ____|_____|____
        |     |
        |  O  |
    """

    board = Board()

    assert board.get_available_moves() == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert board.player == Player.X
    assert board.move_count == 0
    assert board.move_history == []
    assert board.game_result is None

    board.make_move(0)  # X
    assert board.get_available_moves() == [1, 2, 3, 4, 5, 6, 7, 8]
    assert board.player == Player.O
    assert board.move_count == 1
    assert board.move_history == [0]
    assert board.game_result is None

    board.make_move(4)  # O
    assert board.get_available_moves() == [1, 2, 3, 5, 6, 7, 8]
    assert board.player == Player.X
    assert board.move_count == 2
    assert board.move_history == [0, 4]
    assert board.game_result is None

    board.make_move(1)  # X
    assert board.get_available_moves() == [2, 3, 5, 6, 7, 8]
    assert board.player == Player.O
    assert board.move_count == 3
    assert board.move_history == [0, 4, 1]
    assert board.game_result is None

    board.make_move(7)  # O
    assert board.get_available_moves() == [2, 3, 5, 6, 8]
    assert board.player == Player.X
    assert board.move_count == 4
    assert board.move_history == [0, 4, 1, 7]
    assert board.game_result is None

    board.make_move(2)  # X
    assert board.get_available_moves() == [3, 5, 6, 8]
    assert board.player == Player.O
    assert board.move_count == 5
    assert board.move_history == [0, 4, 1, 7, 2]
    assert board.game_result == Result.X_WON

    board.undo_move()
    assert board.get_available_moves() == [2, 3, 5, 6, 8]
    assert board.player == Player.X
    assert board.move_count == 4
    assert board.move_history == [0, 4, 1, 7]
    assert board.game_result is None
