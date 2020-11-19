import chess
import parse_input as parser

board = chess.Board()
board.reset()
print(board)
while True:
    if board.is_checkmate():
        print("Checkmate")
        break
    st_in = parser.parse_to_valid_chess_move(input())
    mov = chess.Move.null() if st_in.lower() == "skip" else chess.Move.from_uci(st_in)
    if mov == chess.Move.null() or mov in board.legal_moves:
        board.push(mov)
        print(board)
    elif board.is_check():
        print("Cannot make this move - you are in check.")
    else:
        print("Illegal move")