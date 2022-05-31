from src.board import Board
from src.game import Game

if __name__ == "__main__":
    board = Board()
    game = Game(board)

    game.play()
