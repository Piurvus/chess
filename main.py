from view.chessboard import ChessBoard
from model.board import Board
from control.controller import Controller


def main():
    board = Board()
    view = ChessBoard(board)
    controller = Controller(board, view)
    controller.run()


if __name__ == '__main__':
    main()
