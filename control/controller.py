from model.board import Board
from view.chessboard import ChessBoard
from model.pieces import Pieces


class Controller:


    def __init__(self, board: Board, view: ChessBoard) -> None:
        self.board = board
        self.view = view
        self.view.bindClick(self.squareClick)
        self.view.drawBoard()


    def run(self) -> None:
        self.view.mainloop()




    def squareClick(self, row: int, col: int, event=None) -> None:
        print('yep works', row, col)

        self.view.placePiece(row, col, Pieces.BKing)
