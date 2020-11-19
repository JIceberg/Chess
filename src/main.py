import chess
import chess.svg
from parse_input import *
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from tkinter import *

def __create_board_png():
    f = open("generated/board.svg", "w+")
    f.write(chess.svg.board(board))
    f.close()
    drawing = svg2rlg("generated/board.svg")
    renderPM.drawToFile(drawing, "generated/board.png", fmt="PNG")

board = chess.Board()
board.reset()
__create_board_png()

gui = Tk()
gui.title("Chess")
move = StringVar()  # global

from PIL import Image, ImageTk

def run():

    if board.is_game_over():
        if board.is_checkmate():
            print("Checkmate")
        else:
            print("Game over")
        return
    
    mov = chess.Move.null()
    if not (mov := parse_to_valid_chess_move(move.get())) or board.is_legal(mov):
        if not mov: print("Skipped turn")
        board.push(mov)
        __create_board_png()
        global _pimg
        _pimg = ImageTk.PhotoImage(Image.open('generated/board.png'))
        frame.itemconfig(game_img, image = _pimg)
    elif board.is_check():
        print("Cannot make this move - you are in check.")
    else:
        print("Illegal move")

__create_board_png()

input_label = Label(gui, text="Your Turn")
input_label.pack(side = TOP)
section = Frame(gui)
section.pack(side = TOP)
user_input = Entry(section, textvariable=move)
user_input.pack(side = LEFT)
play_button = Button(section, text='Move', command=run)
play_button.pack(side = RIGHT)

img = Image.open('generated/board.png')
pimg = ImageTk.PhotoImage(img)
size = img.size

frame = Canvas(gui, width=size[0], height=size[1])
game_img = frame.create_image(0, 0, anchor='nw', image=pimg)
frame.pack()

gui.mainloop()
