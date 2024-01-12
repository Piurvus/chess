from view.chessboard import ChessBoard
from model.board import Board


def main():
    board = Board()
    print(board.bitboards)
    view = ChessBoard()
    view.mainloop()


if __name__ == '__main__':
    main()
