import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

from view.piece_manager import Piece_manager
from model.pieces import Pieces
from model.board import Board

from typing import Callable
from functools import partial

class ChessBoard(tk.Tk):


    def __init__(self, model:Board) -> None:
        super().__init__()
        self.title("Chess")
        self.attributes('-type', 'dialog')
        self.clickcalls = []

        self.initialize_styles()
        self.build_board()
        self.geometry("1000x1000")

        self.model = model

    def initialize_styles(self):
        '''
        Prepares the styles for squares used in build_board
        Creates white.TFrame and black.TFrame

        '''
        # Frame styles
        style = ttk.Style()
        style.configure(
            'white.TFrame',
            background='white',
            boarderwidth=0,
            relief='flat',
        )

        style.configure(
            'black.TFrame',
            background='grey',
            boarderwidth=0,
            relief='flat',
        )

        # Label styles
        self.font = tkfont.Font(family='Arial', size=20, weight='bold')
        style.configure(
            'board.TLabel',
            foreground='black',
            font=self.font,
            anchor=tk.CENTER
        )

    def build_board(self) -> None:
        '''
        Building the board in a tkinter frame widget
        '''

        self.board = ttk.Frame(self)

        # create the chessboard
        self.grid = []
        for i in range(8):
            cols = []
            for j in range(8):
                curr_style = ('white' if (i + j) % 2 == 0 else 'black') + '.TFrame'
                f = ttk.Frame(self.board, width=100, height=100, style=curr_style)
                f.grid(row=i, column=j + 1)
                f.grid_propagate(False)

                cols.append(f)
            self.grid.append(cols)
        # reverse order of rows to make sure that
        # (0, 0) corresponds to the bottom left
        self.grid = self.grid[::-1]

        # create numbering 1-8 and A-H
        for i in range(8, 0, -1):
            f1 = ttk.Frame(self.board, width=100, height=100)
            f2 = ttk.Frame(self.board, width=100, height=100)

            f1.grid(row=i - 1, column=0)
            f2.grid(row=8, column=i)

            # make sure the label isn't overwritten
            f1.grid_propagate(False)
            f2.grid_propagate(False)

            l1 = ttk.Label(f1, text=str(i), style='board.TLabel')
            l2 = ttk.Label(f2, text=str(chr(ord('a') + i - 1)), style='board.TLabel')

            # center the labels
            l1.place(anchor=tk.CENTER, relx=.8, rely=.5)
            l2.place(anchor=tk.CENTER, relx=.5, rely=.2)


        self.board['padding'] = 20
        self.board.grid()

    def drawBoard(self) -> None:
        for i, piece in enumerate(Pieces):
            current_piece = self.model.bitboards[i]

            for j, bit in enumerate(reversed(bin(current_piece)[2:])):
                if int(bit) == 0:
                    continue
                Piece_manager.place_piece(self.grid[j // 8][j % 8], piece, self.clickcalls[j//8][j%8])

    def placePiece(self, i: int, j: int, piece: Pieces) -> None:
        Piece_manager.place_piece(self.grid[i][j], piece, self.clickcalls[i][j])

    def bindClick(self, callback: Callable[[int, int, tk.Event], None]) -> None:
        self.clickcalls = []
        for i in range(8):
            cs = []
            for j in range(8):
                cs.append(partial(callback, i, j))
                self.grid[i][j].bind("<Button-1>", cs[j])
            self.clickcalls.append(cs)

    def close(self, _: tk.Event) -> None:
        '''
        Closes the window
        '''

        self.destroy()
