from typing import Tuple
from src.constants import Player
from src.ai import Minimax
from src.board import Board
from src.game import Game
from src.utils import get_other_player, get_random_player


def _setup_players() -> Tuple[Player, Player]:
    human_player: Player = get_random_player()
    ai_player: Player = get_other_player(human_player)

    return human_player, ai_player


if __name__ == "__main__":
    human, ai = _setup_players()

    board = Board(player=human)
    ai: Minimax = Minimax(board, player=ai)

    game = Game(board, ai)

    game.play()
