from model.pieces import Pieces
from model.pieces import get_moves


class Board:

    bitboards = [0 for _ in range(len(Pieces))]

    def __init__(self) -> None:
        self.prepare()


    def prepare(self) -> None:
        '''
        Creates one bitboard per piece.
        '''

        # initialize bitboard to starting position

        self.bitboards[Pieces.WPawn.value] = 0xff << 8
        self.bitboards[Pieces.BPawn.value] = 0xff << 8 * 6

        self.bitboards[Pieces.WKing.value] = 1 << 4
        self.bitboards[Pieces.BKing.value] = 1 << 4 + 7 * 8

        self.bitboards[Pieces.WQueen.value] = 1 << 3
        self.bitboards[Pieces.BQueen.value] = 1 << 3 + 7 * 8

        self.bitboards[Pieces.WRook.value] = 0x81
        self.bitboards[Pieces.BRook.value] = 0x81 << 7 * 8

        self.bitboards[Pieces.WBishop.value] = 0x24
        self.bitboards[Pieces.BBishop.value] = 0x24 << 7 * 8

        self.bitboards[Pieces.WKnight.value] = 0x42
        self.bitboards[Pieces.BKnight.value] = 0x42 << 7 * 8

    def occupied(self, row:int, col:int) -> Pieces:
        '''
        Checks if a given square is occupied or not.
        If the square is occupied, returns Pieces.Invalid else returns
        the piece.
        '''
        index = row*8 + col
        for k, bits in enumerate(self.bitboards):
            if (bits | (1 << index)) == bits:
                return Pieces.getPiece(k)
        return Pieces.getPiece(-1)

    def getMoves(self, row:int, col:int) -> int:
        '''
        Given a square, this function returns all possible moves 
        for the piece on the given square as an integer.
        '''

        piece = self.occupied(row, col)
        index = row*8 + col

        white = 0
        black = 0
        for k, bits in enumerate(self.bitboards):
            if k < len(Pieces)//2:
                white |= bits
            else:
                black |= bits

        return get_moves(piece, index, white, black) 
        
        
