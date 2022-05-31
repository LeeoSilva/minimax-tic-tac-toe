from src.board import Board
from src.constants import Result
from src.utils import clear_terminal


class Game:
    board: Board

    def __init__(self, board: Board) -> None:
        self.board = board

    def setup(self) -> None:
        """Set's up the game initial game state.
        Should run only once and before the game_loop method.
        """
        clear_terminal()
        # self.board._random_player_starts()

    def game_loop(self) -> None:
        """This function should execute every game tick."""
        self.board.render()

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
                print(exc)

        self.display_end()

    def display_end(self):
        if self.board.fetch_game_result() == Result.X_WON:
            print("X WON")
            # TODO: save statistics in a file.

        elif self.board.fetch_game_result() == Result.O_WON:
            print("O WON")
            # TODO: save statistics in a file.
        else:
            print("STALEMATE")
            # TODO: save statistics in a file.

    def get_player_input(self) -> str:

        # self.display_statistics() TODO

        return int(input("Make your move: "))
