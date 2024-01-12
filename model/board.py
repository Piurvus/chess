from model.pieces import Pieces


class Board:

    bitboards = [0 for _ in range(12)]

    def __init__(self):

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

        print(bin(0xff << 8 | 1 << 4 | 1 << 3 | 0x81 | 0x24 | 0x42))
