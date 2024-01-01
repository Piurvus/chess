from enum import Enum, unique


@unique
class Pieces(Enum):
    WKing = 0
    WQueen = 1
    WBishop = 2
    WKnight = 3
    WRook = 4
    WPawn = 5

    BKing = 6
    BQueen = 7
    BBishop = 8
    BKnight = 9
    BRook = 10
    BPawn = 11
