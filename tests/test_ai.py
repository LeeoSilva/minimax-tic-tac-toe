import numpy as np
from src.board import Board, Player, Result
from src.ai import Minimax


def test_best_move():
    board_state = np.array(
        [
            [Player.X, Player.O, Player.EMPTY],
            [Player.EMPTY, Player.X, Player.O],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY],
        ]
    )

    board = Board(state=board_state)
    ai = Minimax(board=board, player=Player.O)

    ai.make_best_move()

    assert board.fetch_game_result() == Result.X_WON
