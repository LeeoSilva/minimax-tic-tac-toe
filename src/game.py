from src.board import Board
from src.constants import Result, Player
from src.utils import clear_terminal, get_random_player
from src.ai import Minimax


class Game:
    board: Board
    ai: Minimax

    def __init__(self, board: Board, ai: Minimax) -> None:
        self.board = board
        self.ai = ai

    def setup(self) -> None:
        """Set's up the game initial game state.
        Should run only once and before the game_loop method.
        """
        clear_terminal()

    def game_loop(self) -> None:
        """This function should execute every game tick."""
        self.board.render()

        if self.board.player is self.ai.player:
            move = self.ai.make_best_move()
        else:
            move = self.get_player_input()

        self.board.make_move(move)

    def play(self) -> None:
        """Set's up and initializes the game handling the game loop and players inputs.
        Every game tick is ran after the player input.
        """
        self.setup()

        while not self.board.is_game_over():
            try:
                self.game_loop()
                clear_terminal()
            except Exception as exc:
                clear_terminal()

        # Final render.
        clear_terminal()
        self.board.render()
        self.display_end()

    def display_end(self):
        if self.board.fetch_game_result() == self.board.player:
            print("The human won.")
            # TODO: save statistics in a file.

        elif self.board.fetch_game_result() == self.ai.player:
            print("The AI won.")
            # TODO: save statistics in a file.
        else:
            print("Stalemate")
            # TODO: save statistics in a file.

    def get_player_input(self) -> str:

        # self.display_statistics() TODO

        return int(input("Make your move: "))
