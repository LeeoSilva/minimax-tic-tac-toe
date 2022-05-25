import numpy as np


class Board:
    def __init__(self, state: list = np.full((3, 3), "_")) -> None:
        self.state = state
        self.winner = ""

    def evaluate(self) -> None:
        """Should evaluate if the board is valid or not.
        e.g.: A board with the following state is invalid:
                X | X | X
                X | O | X
                O | O | O
        """
        pass

    def set_winner(self, winner: str) -> None:
        if ["X", "O"] not in winner:
            raise ValueError("The winner can only be X or O.")

        self.winner = winner

    def get_winner(self) -> str:
        return self.winner

    def get_state(self):
        return self.state.tolist()

    def render(self) -> None:
        pass

    def check_win(self) -> str:
        self.evaluate()

        self.check_horizontal_for_win()
        self.check_vertical_for_win()
        self.check_primary_diagonal_for_win()
        self.check_secondary_diagonal_for_win()

        return self.get_winner()

    def check_primary_diagonal_for_win(self) -> None:
        diagonal = self.state.diagonal()
        if np.all(diagonal == diagonal[0]):
            self.winner = diagonal[0]

    def check_secondary_diagonal_for_win(self) -> None:
        secundary_diagonal = np.diag(np.fliplr(self.state))
        if np.all(secundary_diagonal == secundary_diagonal[0]):
            self.winner = secundary_diagonal[0]

    def check_horizontal_for_win(self) -> None:
        for row in self.state:
            if np.all(row == row[0]):
                self.winner = row[0]

    def check_vertical_for_win(self) -> None:
        for idx, _ in enumerate(self.state):
            vertical = self.state[:, idx]
            if np.all(vertical == vertical[0]):
                self.winner = vertical[0]
