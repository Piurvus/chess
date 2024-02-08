from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk

from model.pieces import Pieces



def static_init(cls):
    cls.init()
    return cls

@static_init
class Piece_manager:
    '''
    Static Class to manage the logic for updating frames to include images.
    Loads and crops the image such that the chess pieces can be used.
    '''

    @classmethod
    def init(cls):
        '''
        Opening and cropping as well as resizing of the image, such that
        chess pieces can be placed on frames
        '''
        fullimg = Image.open('resources/pieces2.png')
        # White: King Queen Bishop Knight Rook
        # Black: Same

        cls.pieces_pre = [fullimg for _ in Pieces]
        cls.pieces = {}
        for i, _ in enumerate(Pieces):
            s = len(Pieces) // 2

            crop_shape = (
                334 * (i % s),
                334 * (i // s),
                334 * (i % s + 1),
                334 * (i // s + 1)
            )

            cls.pieces_pre[i] = fullimg.crop(crop_shape)
            cls.pieces_pre[i] = cls.pieces_pre[i].resize((100, 100))


    @classmethod
    def get_img(cls, piece: Pieces) -> ImageTk.PhotoImage:
        '''
        If necessary loads the PhotoImage of the Piece
        PhotoImage apparently needs an active tkinter main loop.
        '''
        if piece.name not in cls.pieces:
            cls.pieces[piece.name] = ImageTk.PhotoImage(cls.pieces_pre[piece.value])
        return cls.pieces[piece.name]


    @classmethod
    def place_piece(cls, frame: tk.Frame, piece: Pieces, callback) -> None:
        '''
        Given a frame and a piece, places the piece into the frame.
        Old pieces in the frame are destroyed!
        '''

        # clean up frame
        for child in frame.winfo_children():
            child.destroy()
        assert(len(frame.winfo_children()) == 0)

        # place new piece
        img = cls.get_img(piece)

        color = (ttk.Style().lookup((frame)['style'], 'background'))
        label = tk.Label(frame, bg=color, image=img, relief='flat', borderwidth=0)
        label.pack()

        label.bind("<Button-1>", callback)

    # staticmethod
