from math import inf
from src.constants import Result


class Minimax:
    def __init__(self, board, player) -> None:
        self.board = board
        self.player = player

    def make_best_move(self):
        best_score = -inf
        best_move = None

        for move in self.board.get_available_moves():
            self.board.make_move(move)

            score = self.minimax(self._is_maximizers_turn(), self.player)

            self.board.undo_move()

            if score > best_score:
                best_score = score
                best_move = move

        self.board.make_move(best_move)

    def minimax(self, is_maximizer_turn: bool, maximizer_target):
        end_game = self.board.fetch_game_result()

        if end_game is Result.STALEMATE:
            return 0
        elif end_game in [Result.X_WON, Result.O_WON]:
            return 1 if self.board.get_winner() is maximizer_target else -1

        scores = []
        for move in self.board.get_available_moves():
            self.board.make_move(move)

            tree_scores = self.minimax(not is_maximizer_turn, maximizer_target)

            scores.append(tree_scores)

            self.board.undo_move()

            if (is_maximizer_turn and max(scores) == 1) or (
                not is_maximizer_turn and min(scores) == -1
            ):
                break

        return max(scores) if maximizer_target else min(scores)

    def _is_maximizers_turn(self) -> bool:
        return self.board.player_turn == self.player

    def calculate_score_of_winner(self):
        winner = self.board.get_winner()
        if winner is self.player:
            return 1
        elif winner is not self.player:
            return -1
