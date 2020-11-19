# -- String is in form "Position" -> "Position" -- #
def parse_to_valid_chess_move(i: str) -> str:
    return i if i.lower() == "SKIP" else (i[0:2] + i[len(i)-2:len(i)])