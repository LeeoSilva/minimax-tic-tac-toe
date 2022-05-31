from src.board import Board


class Game:
    board: Board

    def __init__(self, board: Board) -> None:
        self.board = board

    def setup(self) -> None:
        """Set's up the game initial game state.
        Should run only once and before the game_loop method.
        """
        self.board._create_default_board()
        self.board._random_player_starts()

    def game_loop(self) -> None:
        """This function should execute every game tick."""
        move = self.get_player_move()
        self.board.make_move(move)

    def play(self) -> None:
        """Set's up and initializes the game handling the game loop and players inputs.
        Every game tick is ran after the player input.
        """
        self.setup()

        while self.board.check_stalemate():
            self.game_loop()
