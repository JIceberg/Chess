import chess
import chess.svg
from parse_input import *
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

board = chess.Board()
board.reset()

'''
while True:
    if board.is_checkmate():
        print("Checkmate")
        break
    st_in = parse_to_valid_chess_move(input())
    mov = chess.Move.null() if st_in.lower() == "skip" else chess.Move.from_uci(st_in)
    if mov == chess.Move.null() or mov in board.legal_moves:
        board.push(mov)
        print(board)
    elif board.is_check():
        print("Cannot make this move - you are in check.")
    else:
        print("Illegal move")
'''

f = open("generated/board.svg", "w+")
f.write(chess.svg.board(board))
f.close()

drawing = svg2rlg("generated/board.svg")
renderPM.drawToFile(drawing, "generated/board.png", fmt="PNG")

from tkinter import *
gui = Tk()
gui.title("Chess")

from PIL import Image, ImageTk
img = Image.open('generated/board.png')
pimg = ImageTk.PhotoImage(img)
size = img.size

frame = Canvas(gui, width=size[0], height=size[1])
frame.pack()
frame.create_image(0, 0, anchor='nw', image=pimg)

gui.mainloop()
