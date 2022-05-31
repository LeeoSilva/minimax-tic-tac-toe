import enum
import random

import numpy as np

from src.constants import BOARD_COLS, BOARD_ROWS, Player, Result
from src.utils import get_max_move_count


class Board:
    state: np.ndarray
    player: Player
    move_count: int
    move_history: list
    game_result: Result

    def __init__(
        self,
        player: Player,
        state: np.ndarray = np.zeros((BOARD_ROWS, BOARD_COLS), dtype=int),
    ) -> None:
        self.state = np.copy(state)
        self.player = player
        self.move_count = 0
        self.move_history = []
        self.game_result = None

        self.update_move_count()

    def update_move_count(self) -> None:
        x_move_count: int = np.count_nonzero(self.state == Player.X)
        o_move_count: int = np.count_nonzero(self.state == Player.O)

        self.move_count = x_move_count + o_move_count

    def check_stalemate(self) -> None:
        if self.move_count >= get_max_move_count():
            self.game_result = Result.STALEMATE

    def make_move(self, move: int) -> None:
        self.move_contraint(move)
        coord = np.unravel_index(move, (BOARD_ROWS, BOARD_COLS))
        self.state[coord] = int(self.player)
        self.move_count += 1
        self.move_history.append(move)
        self.next_player()
        self.is_game_over()

    def move_contraint(self, move) -> None:
        if move is None:
            raise AttributeError("Invalid Move.")

        if self.is_game_over():
            raise AttributeError("Game is already over.")

        if move not in self.get_available_moves():
            raise AttributeError(f"Move {move} is not an available move!")

        if move not in range(0, 10):
            raise AttributeError(f"Move `{move}` is an Ilegal move!")

    def get_winner(self) -> Player:
        if self.fetch_game_result() is Result.X_WON:
            return Player.X
        elif self.fetch_game_result() is Result.O_WON:
            return Player.O
        else:
            return None

    def get_available_moves(self) -> list:
        coords = np.where(self.state == Player.EMPTY)
        coords = np.ravel_multi_index(coords, (BOARD_ROWS, BOARD_COLS))
        return coords.tolist()

    def fetch_game_result(self) -> Result:
        return self.game_result

    def undo_move(self) -> None:
        coords = self.move_history[-1]
        coords = np.unravel_index(coords, (BOARD_ROWS, BOARD_COLS))
        del self.move_history[-1]

        self.state[coords] = Player.EMPTY
        self.game_result = None
        self.move_count -= 1
        self.next_player()

    def set_game_result(self, winner: Player) -> None:
        if winner in Player:
            raise AttributeError(f"Winner `{winner}` is an invalid player.")

        if winner is Player.EMPTY:
            raise AttributeError(f"Winner cannot be an empty player.")

        if winner == Player.X:
            return self.x_won()

        return self.o_won()

    def x_won(self) -> None:
        self.game_result = Result.X_WON

    def o_won(self) -> None:
        self.game_result = Result.O_WON

    def stalemate(self) -> None:
        self.game_result = Result.STALEMATE

    def get_state(self) -> list:
        return self.state.tolist()

    def render(self) -> None:
        for row in self.state:
            for item in row:
                if item == Player.X:
                    print("| X |", end=" ")
                elif item == Player.O:
                    print("| O |", end=" ")
                else:
                    print(f"| □ |", end=" ")
            print("")

    def is_game_over(self) -> bool:
        self.check_stalemate()

        self.check_horizontal()
        self.check_vertical()
        self.check_diagonal()
        self.check_anti_diagonal()

        return self.fetch_game_result() is not None

    def check_diagonal(self) -> None:
        diagonal = self.state.diagonal()
        if self.check_three(diagonal):
            return self.set_game_result(diagonal[0])

    def check_anti_diagonal(self) -> None:
        anti_diagonal = np.diag(np.fliplr(self.state))
        if self.check_three(anti_diagonal):
            return self.set_game_result(anti_diagonal[0])

    def check_horizontal(self) -> None:
        for row in self.state:
            if self.check_three(row):
                return self.set_game_result(row[0])

    def check_vertical(self) -> None:
        for idx, _ in enumerate(self.state):
            vertical = self.state[:, idx]
            if self.check_three(vertical):
                return self.set_game_result(vertical[0])

    def check_three(self, combination) -> bool:
        return combination[0] != Player.EMPTY and np.all(combination == combination[0])

    def next_player(self) -> None:
        """Handles next player logic."""
        if self.player == Player.X:
            return self.o_turn()

        return self.x_turn()

    def x_turn(self) -> None:
        self.player = Player.X

    def o_turn(self) -> None:
        self.player = Player.O

    def _random_player_starts(self) -> Player:
        """Gets a random player to start the game."""
        players = [Player.X, Player.O]
        self.player = random.choise(players)
        return self.player
