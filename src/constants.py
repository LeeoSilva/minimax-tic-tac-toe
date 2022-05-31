from enum import EnumMeta, IntEnum


# dimensions of the board.
BOARD_ROWS: int = 3
BOARD_COLS: int = 3


class BaseEnum(EnumMeta):
    def __contains__(cls, value):
        return value in cls.__members__.items()


class Player(IntEnum, metaclass=BaseEnum):
    """Player values."""

    EMPTY = 0
    X = 1
    O = 2


class Result(IntEnum, metaclass=BaseEnum):
    """Enum of possible results for the game."""

    STALEMATE = 0
    X_WON = 1
    O_WON = 2
