
from typing import Callable

class Mover():
    '''
    Move generation functions.
    Given a position and white and black pieces, all possible moves 
    will be returned as integer (bitboard representation)
    '''

    @staticmethod
    def swap(func: Callable[[int, int, int], int], position: int, white: int, black: int) -> int:
        '''
        Changes the arguments such that the normal func can be called,
        regardless of the piece color.
        '''

        new_position = position
        new_white = white
        new_black = black
        return func(new_position, new_white, new_black)

    @staticmethod
    def moveKing(position:int, white:int, black:int) -> int:
        return 0

    @staticmethod
    def moveQueen(position:int, white:int, black:int) -> int:
        return 0

    @staticmethod
    def moveBishop(position:int, white:int, black:int) -> int:
        return 1000

    @staticmethod
    def moveKnight(position:int, white:int, black:int) -> int:
        return 0

    @staticmethod
    def moveRook(position:int, white:int, black:int) -> int:
        return 0

    @staticmethod
    def movePawn(position:int, white:int, black:int) -> int:
        return 1
