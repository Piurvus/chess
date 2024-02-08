from model.board import Board
from view.chessboard import ChessBoard
from model.pieces import Pieces


class Controller:


    def __init__(self, board: Board, view: ChessBoard) -> None:
        self.board = board
        self.view = view
        self.view.bindClick(self.squareClick)
        self.view.drawBoard()

        self.active = None


    def run(self) -> None:
        self.view.mainloop()




    def squareClick(self, row: int, col: int, event=None) -> None:

        print('yep works', row, col, event)

        #self.view.placePiece(row, col, Pieces.BKing)

        if self.active == (row, col):
            self.view.highlightSquare(row, col, False)
            self.active = None
        elif self.active is None:
            self.view.highlightSquare(row, col, True)
            self.active = (row, col)
