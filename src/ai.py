from math import inf
from os import O_WRONLY
from unittest import result
from src.board import Board
from src.constants import Player, Result
from abc import ABCMeta


class BaseAI(ABCMeta):
    board: Board
    player: Player


class Minimax(BaseAI):
    def __init__(self, board, player) -> None:
        self.board = board
        self.player = player

    def make_best_move(self):
        bestScore = -inf
        bestMove = None

        for move in self.board.get_available_moves():
            self.board.make_move(move)

            score = self.minimax(False, self._is_maximizers_turn())

            self.board.undo_move()

            if score > bestScore:
                bestScore = score
                bestMove = move

        self.board.make_move(bestMove)

    def minimax(self, is_maximizer_turn: bool, maximizer_target):
        end_game = self.board.fetch_game_result()

        if end_game is Result.STALEMATE:
            return 0
        elif end_game in [Result.X_WON, Result.O_WON]:
            return self.calculate_score_of_winner()

        scores = []
        for move in self.board.get_available_moves():
            self.board.make_move(move)

            scores.append(self.minimax(not is_maximizer_turn, maximizer_target))

            self.board.undo_move()

            if self._we_are_losing(is_maximizer_turn, scores):
                break

        return max(scores) if maximizer_target else min(scores)

    def _we_are_losing(self, is_maximizer_target, scores):
        return (is_maximizer_target and max(scores) == 1) or (
            not is_maximizer_target and min(scores) == -1
        )

    def _is_maximizers_turn(self) -> bool:
        return self.board.player == self.player

    def calculate_score_of_winner(self):
        winner = self.board.get_winner()
        if winner is self.player:
            return 1
        elif winner is not self.player:
            return -1
