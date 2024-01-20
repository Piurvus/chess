from model.pieces import Pieces


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

    def occupied(self, row:int, col:int) -> int:
        '''
        Checks if a given square is occupied or not.
        If the square is occupied, returns -1 else returns
        the number of the number of the piece.
        '''
        index = row*8 + col
        for k, bits in enumerate(self.bitboards):
            if (bits | (1 << index)) == bits:
                return k
        return -1
