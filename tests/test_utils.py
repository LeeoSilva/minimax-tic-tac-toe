from src.utils import get_other_player, get_random_player
from src.constants import Player


def test_get_random_player():
    player = get_random_player()
    assert player in [Player.X, Player.O]


def test_get_other_player():
    assert get_other_player(Player.X) == Player.O
    assert get_other_player(Player.O) == Player.X
