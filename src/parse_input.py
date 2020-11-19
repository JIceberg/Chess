import chess
import re

def __parse(s: str) -> chess.Move:
    # return arbitrary invalid move
    if not re.match('^[A-Za-z]\d, [A-Za-z]\d', s): return chess.Move.null()

    tmp = s.split(', ')
    return chess.Move.from_uci(tmp[0].lower()+tmp[1].lower()+tmp[2]) if len(tmp) > 2 else chess.Move.from_uci(tmp[0].lower()+tmp[1].lower())

def parse_to_valid_chess_move(i: str) -> chess.Move:
    '''
    String is in form "{position}, {position}, opt:{piece symbol}"
    Positions are a letter followed by a number.
    The piece symbol is an uppercase or lowercase letter representing the piece and color
    Uppercase = white, lowercase = black

    P: chess.PAWN
    N: chess.KNIGHT
    B: chess.BISHOP
    K: chess.KING
    R: chess.ROOK
    Q: chess.QUEEN
    '''
    return chess.Move.null() if i.lower() == "skip" else __parse(i)
