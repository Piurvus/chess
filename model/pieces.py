from enum import Enum, unique
from functools import partial
from model.moveGenerator import Mover


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

    Invalid = -1


    @classmethod
    def getPiece(cls, key):
        '''
        Helper function to lookup values for their Piece.
        '''
        if isinstance(key, int):
            for piece in Pieces:
                if piece.value == key:
                    return piece
        raise KeyError(f"Class {cls.__name__} does not have piece {key}")



'''
Piece to function mapping.
'''
moves_function = {
    Pieces.WKing: Mover.moveKing,
    Pieces.WQueen: Mover.moveQueen, 
    Pieces.WBishop: Mover.moveBishop,
    Pieces.WKnight: Mover.moveKnight,
    Pieces.WRook: Mover.moveRook,
    Pieces.WPawn: Mover.movePawn,

    Pieces.BKing: partial(Mover.swap, Mover.moveKing),
    Pieces.BQueen: partial(Mover.swap, Mover.moveQueen), 
    Pieces.BBishop: partial(Mover.swap, Mover.moveBishop),
    Pieces.BKnight: partial(Mover.swap, Mover.moveKnight),
    Pieces.BRook: partial(Mover.swap, Mover.moveRook),
    Pieces.BPawn: partial(Mover.swap, Mover.movePawn),
}


def get_moves(piece: Pieces, position: int, white: int, black: int) -> int:
    '''
    Given the enum value, position, white and black boards, the function will call 
    the right function to return all possible moves.
    '''
    assert piece.value < len(Pieces) and piece.value >= 0

    func = moves_function.get(piece, lambda a, b, c: (a+b+c)*0 -1 )
    return func(position, white, black)


