from tkinter import *
import re
import os
from time import sleep


# Set piece variables
bR = {'piece': 'r', 'color': 'black'}
bB = {'piece': 'b', 'color': 'black'}
bN = {'piece': 'n', 'color': 'black'}
bQ = {'piece': 'q', 'color': 'black'}
bK = {'piece': 'k', 'color': 'black'}
bP = {'piece': 'p', 'color': 'black'}
na = {'piece': ' ', 'color': 'none'}
wR = {'piece': 'R', 'color': 'white'}
wB = {'piece': 'B', 'color': 'white'}
wN = {'piece': 'N', 'color': 'white'}
wQ = {'piece': 'Q', 'color': 'white'}
wK = {'piece': 'K', 'color': 'white'}
wP = {'piece': 'P', 'color': 'white'}

# Set rows 2d List (tells what each space contains currently)
rows = [[bR, bN, bB, bQ, bK, bB, bN, bR],
        [bP, bP, bP, bP, bP, bP, bP, bP],
        [na, na, na, na, na, na, na, na],
        [na, na, na, na, na, na, na, na],
        [na, na, na, na, na, na, na, na],
        [na, na, na, na, na, na, na, na],
        [wP, wP, wP, wP, wP, wP, wP, wP],
        [wR, wN, wB, wQ, wK, wB, wN, wR]]


# Define current board with colorama colors
def current_board():
    row8 = f"│  {rows[0][0]['piece']}  │  {rows[0][1]['piece']}  " \
           f"│  {rows[0][2]['piece']}  │  {rows[0][3]['piece']}  " \
           f"│  {rows[0][4]['piece']}  │  {rows[0][5]['piece']}  " \
           f"│  {rows[0][6]['piece']}  │  {rows[0][7]['piece']}  │"
    row7 = f"│  {rows[1][0]['piece']}  │  {rows[1][1]['piece']}  " \
           f"│  {rows[1][2]['piece']}  │  {rows[1][3]['piece']}  " \
           f"│  {rows[1][4]['piece']}  │  {rows[1][5]['piece']}  " \
           f"│  {rows[1][6]['piece']}  │  {rows[1][7]['piece']}  │"
    row6 = f"│  {rows[2][0]['piece']}  │  {rows[2][1]['piece']}  " \
           f"│  {rows[2][2]['piece']}  │  {rows[2][3]['piece']}  " \
           f"│  {rows[2][4]['piece']}  │  {rows[2][5]['piece']}  " \
           f"│  {rows[2][6]['piece']}  │  {rows[2][7]['piece']}  │"
    row5 = f"│  {rows[3][0]['piece']}  │  {rows[3][1]['piece']}  " \
           f"│  {rows[3][2]['piece']}  │  {rows[3][3]['piece']}  " \
           f"│  {rows[3][4]['piece']}  │  {rows[3][5]['piece']}  " \
           f"│  {rows[3][6]['piece']}  │  {rows[3][7]['piece']}  │"
    row4 = f"│  {rows[4][0]['piece']}  │  {rows[4][1]['piece']}  " \
           f"│  {rows[4][2]['piece']}  │  {rows[4][3]['piece']}  " \
           f"│  {rows[4][4]['piece']}  │  {rows[4][5]['piece']}  " \
           f"│  {rows[4][6]['piece']}  │  {rows[4][7]['piece']}  │"
    row3 = f"│  {rows[5][0]['piece']}  │  {rows[5][1]['piece']}  " \
           f"│  {rows[5][2]['piece']}  │  {rows[5][3]['piece']}  " \
           f"│  {rows[5][4]['piece']}  │  {rows[5][5]['piece']}  " \
           f"│  {rows[5][6]['piece']}  │  {rows[5][7]['piece']}  │"
    row2 = f"│  {rows[6][0]['piece']}  │  {rows[6][1]['piece']}  " \
           f"│  {rows[6][2]['piece']}  │  {rows[6][3]['piece']}  " \
           f"│  {rows[6][4]['piece']}  │  {rows[6][5]['piece']}  " \
           f"│  {rows[6][6]['piece']}  │  {rows[6][7]['piece']}  │"
    row1 = f"│  {rows[7][0]['piece']}  │  {rows[7][1]['piece']}  " \
           f"│  {rows[7][2]['piece']}  │  {rows[7][3]['piece']}  " \
           f"│  {rows[7][4]['piece']}  │  {rows[7][5]['piece']}  " \
           f"│  {rows[7][6]['piece']}  │  {rows[7][7]['piece']}  │"

    print("┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐")
    print(row8)
    print("├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤")
    print(row7)
    print("├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤")
    print(row6)
    print("├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤")
    print(row5)
    print("├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤")
    print(row4)
    print("├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤")
    print(row3)
    print("├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤")
    print(row2)
    print("├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤")
    print(row1)
    print("└─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘")

    sleep(3)
    screen_clear()


# Wait 3 seconds then clear the console
def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platform
        _ = os.system('cls')


# Locate specific piece in the rows list
def find_pieces(_piece):
    indices = [[x, y] for x, li in enumerate(rows) for y, val in enumerate(li) if val == _piece]
    return indices


# get the diagonals between to points in the matrix
def get_diagonal_points(matrix, start_x, start_y, end_x, end_y):
    # make start_x <= end_x, if you don't need to check, remove this line
    if start_x > end_x:
        start_x, start_y, end_x, end_y = end_x, end_y, start_x, start_y

    result = []
    slope = (end_y - start_y) // (end_x - start_x)
    for i, j in zip(range(start_x, end_x), range(start_y, end_y, slope)):
        result.append(matrix[i][j])
    result = result[1:]
    return result


def get_ver_or_hor_points(matrix, start_rank, start_file, end_rank, end_file):
    # make start_x <= end_x, if you don't need to check, remove this line
    result = []
    if start_rank == end_rank:
        for i in range(min(start_file, end_file), max(start_file, end_file)):
            result.append(matrix[end_rank][i])
    else:
        for j in range(min(start_rank, end_rank), max(start_rank, end_rank)):
            result.append(matrix[j][end_file])
    result = result[1:]
    return result


class App:
    def __init__(self, master):
        root.geometry('600x500')

        self.text = Text(master,
                         width=50,
                         height=25,
                         padx=10,
                         pady=10)
        self.text.pack()

        self.button = Button(master, text="Play", command=self.command)
        self.button.pack()

        self.frame = Frame(master, width=100, height=100)
        self.frame.pack()

    def command(self):
        pgn_list = self.text.get("1.0", 'end-1c').split('\n1.')
        pgn_list[1] = re.sub(' ;.*?[\n]', ' ', pgn_list[1])
        pgn_list[1] = re.sub(r'\(.*?\) ', '', pgn_list[1])
        pgn_list[1] = "1." + re.sub(' {.*?}', '', pgn_list[1])
        pgn_list[1] = pgn_list[1].replace('\n', ' ')
        data_list = list(filter(None, pgn_list[0].split('\n')))
        moves_string = re.sub('( 1/2|[0-1])-(1/2|[0-1])', '',
                              pgn_list[1].replace('\n', '').replace('. ', '.').replace('.', '. '))
        moves_list = [x for x in re.split(r'(.*?\s.*?\s.*?\s)', moves_string) if x]
        moves_dict = {}
        for moves in moves_list:
            moves = moves.replace("+", "")
            key = moves.split(". ")
            moves_dict[key[0]] = key[1].split()

        current_board()

        files = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

        turn = "White"

        def knight_move(_rank, _file, piece, *args):
            file_list = [2, 2, -2, -2, 1, 1, -1, -1]
            rank_list = [1, -1, 1, -1, 2, -2, -2, 2]
            # If both previous_rank and previous_file are passed as arguments
            if len(args) == 2:
                rows[_rank][_file] = piece
                rows[previous_rank][files[str(previous_file)]] = na
                current_board()
            # If only previous_file is passed as an argument
            elif len(args) == 1:
                for i in range(4):
                    try:
                        if rows[_rank + file_list[i]][files[str(previous_file)]] == piece:
                            rows[_rank][_file] = piece
                            rows[_rank + file_list[i]][files[str(previous_file)]] = na
                            current_board()
                    except IndexError:
                        pass
            # Else if neither previous_rank or previous_file are passed as arguments
            else:
                for i in range(8):
                    try:
                        if rows[_rank + rank_list[i]][_file + file_list[i]] == piece:
                            rows[_rank][_file] = piece
                            rows[_rank + rank_list[i]][_file + file_list[i]] = na
                            current_board()
                    except IndexError:
                        pass

        def bishop_move(_rank, _file, piece, *args):
            # If both previous_rank and previous_file are passed as arguments
            if len(args) == 2:
                rows[_rank][_file] = piece
                rows[previous_rank][files[str(previous_file)]] = na
                current_board()
            # If only previous_file is passed as an argument
            elif len(args) == 1:
                current_indices = find_pieces(piece)
                for current_index in current_indices:
                    # If the the square is on a diagonal with the ending square and if the file in each matches
                    if abs(current_index[0] - rank) == abs(current_index[0] - _file) and\
                            previous_file == current_index[1]:
                        rows[_rank][_file] = piece
                        rows[current_index[0]][files[str(previous_file)]] = na
                        current_board()
            # Else if neither previous_rank or previous_file are passed as arguments
            else:
                current_indices = find_pieces(piece)
                for current_index in current_indices:
                    # If the the square is on a diagonal with the ending square
                    if abs(current_index[0] - rank) == abs(current_index[1] - _file) and\
                            all(space == na for space in
                                get_diagonal_points(rows,
                                                    _rank,
                                                    _file,
                                                    current_index[0],
                                                    current_index[1])):
                        rows[_rank][_file] = piece
                        rows[current_index[0]][current_index[1]] = na
                        current_board()

        def rook_move(_rank, _file, piece, *args):
            # If both previous_rank and previous_file are passed as arguments
            if len(args) == 2:
                rows[_rank][_file] = piece
                rows[previous_rank][files[str(previous_file)]] = na
                current_board()
            # If only previous_file or previous_rank is passed as an argument
            elif len(args) == 1:
                current_indices = find_pieces(wR)
                for current_index in current_indices:
                    if files[str(previous_file)] == current_index[1]:
                        rows[_rank][_file] = piece
                        rows[current_index[0]][files[str(previous_file)]] = na
                        current_board()
            # Else if neither previous_rank or previous_file are passed as arguments
            else:
                current_indices = find_pieces(wR)
                for current_index in current_indices:
                    if all(space == na for space in
                           get_ver_or_hor_points(rows, _rank, _file, current_index[0], current_index[1])):
                        rows[_rank][_file] = piece
                        rows[current_index[0]][current_index[1]] = na
                        current_board()
                    else:
                        current_rank_or_file = current_index[1]
                        if all(space == na for space in
                               get_ver_or_hor_points(rows, _rank, _file, current_index[0], current_index[1])):
                            rows[_rank][_file] = piece
                            rows[current_index[0]][current_index[1]] = na
                            current_board()

        for num, moves in moves_dict.items():
            for move in moves:

                if "=" in move:  # This is a pawn promotion
                    rank = 8 - int(move[1])
                    file = ord(move[0]) - 97

                elif "+" in move:  # This is a check
                    rank = 8 - int(move[-2])
                    file = ord(move[-3]) - 97

                elif "#" in move:  # This is a check-mate
                    rank = 8 - int(move[-2])
                    file = ord(move[-3]) - 97

                elif "O-O" in move.upper():  # This is a castle
                    rank = "None"
                    file = "None"

                else:  # This is a regular move (none of the above in the if statement)
                    rank = 8 - int(move[-1])
                    file = ord(move[-2]) - 97

                if "R" in move:  # This is a rook move
                    print(turn + " plays " + move)
                    # If the file of the previous piece is not named in the move
                    if ("x" not in move and len(move) == 3) or ("x" in move and len(move) == 4):
                        if turn == "White":
                            rook_move(rank, file, wR)
                        else:
                            rook_move(rank, file, bR)
                    # Else if the file of the previous piece is named in the move
                    elif ("x" not in move and len(move) == 4) or ("x" in move and len(move) == 5):
                        previous_file = move[1]
                        if turn == "White":
                            rook_move(rank, file, wR, previous_file)
                        else:
                            rook_move(rank, file, bR, previous_file)
                    # Else if both the file and rank are named in the move
                    else:
                        previous_file = move[1]
                        previous_rank = 8 - int(move[2])
                        if turn == "White":
                            rook_move(rank, file, wR, previous_file, previous_rank)
                        else:
                            rook_move(rank, file, bR, previous_file, previous_rank)

                elif "B" in move:  # This is a bishop move
                    print(turn + " plays " + move)
                    # If the file of the previous piece is not named in the move
                    if ("x" not in move and len(move) == 3) or ("x" in move and len(move) == 4):
                        if turn == "White":
                            bishop_move(rank, file, wB)
                        else:
                            bishop_move(rank, file, bB)
                    # Else if the file of the previous piece is named in the move
                    elif ("x" not in move and len(move) == 4) or ("x" in move and len(move) == 5):
                        previous_file = move[1]
                        if turn == "White":
                            bishop_move(rank, file, wB, previous_file)
                        else:
                            bishop_move(rank, file, bB, previous_file)
                    # Else if both the file and rank are named in the move
                    else:
                        previous_file = move[1]
                        previous_rank = 8 - int(move[2])
                        if turn == "White":
                            bishop_move(rank, file, wB, previous_file, previous_rank)
                        else:
                            bishop_move(rank, file, bB, previous_file, previous_rank)

                elif "N" in move:  # This is a knight move
                    print(turn + " plays " + move)
                    # If the file of the previous piece is not named in the move
                    if ("x" not in move and len(move) == 3) or ("x" in move and len(move) == 4):
                        if turn == "White":
                            knight_move(rank, file, wN)
                        else:
                            knight_move(rank, file, bN)
                    # Else if the file of the previous piece is named in the move
                    elif ("x" not in move and len(move) == 4) or ("x" in move and len(move) == 5):
                        previous_file = move[1]
                        if turn == "White":
                            knight_move(rank, file, wN, previous_file)
                        else:
                            knight_move(rank, file, bN, previous_file)
                    # Else if both the file and rank are named in the move
                    else:
                        previous_file = move[1]
                        previous_rank = 8 - int(move[2])
                        if turn == "White":
                            knight_move(rank, file, wN, previous_file, previous_rank)
                        else:
                            knight_move(rank, file, bN, previous_file, previous_rank)

                elif "Q" in move:  # This is a queen move
                    print(turn + " plays " + move)
                    if turn == "White":
                        wq_indices = find_pieces(wQ)
                        rows[rank][file] = wQ
                        rows[wq_indices[0][0]][wq_indices[0][1]] = na
                        current_board()
                    if turn == "Black":
                        bq_indices = find_pieces(bQ)
                        rows[rank][file] = bQ
                        rows[bq_indices[0][0]][bq_indices[0][1]] = na
                        current_board()
                elif "K" in move:  # This is a king move
                    print(turn + " plays " + move)
                    if turn == "White":
                        wk_indices = find_pieces(wK)
                        rows[rank][file] = wK
                        rows[wk_indices[0][0]][wk_indices[0][1]] = na
                        current_board()
                    if turn == "Black":
                        bk_indices = find_pieces(bK)
                        rows[rank][file] = bK
                        rows[bk_indices[0][0]][bk_indices[0][1]] = na
                        current_board()

                elif move == "O-O":  # King-side castle
                    print(turn + " plays " + move)
                    if turn == "White":
                        rows[7][6] = wK
                        rows[7][4] = na
                        rows[7][5] = wR
                        rows[7][7] = na
                        current_board()
                    if turn == "Black":
                        rows[0][6] = bK
                        rows[0][4] = na
                        rows[0][5] = bR
                        rows[0][7] = na
                        current_board()

                elif move == "O-O-O":  # Queen-side castle
                    print(turn + " plays " + move)
                    if turn == "White":
                        rows[7][2] = wK
                        rows[7][4] = na
                        rows[7][3] = wR
                        rows[7][0] = na
                        current_board()
                    if turn == "Black":
                        rows[0][2] = bK
                        rows[0][4] = na
                        rows[0][3] = bR
                        rows[0][0] = na
                        current_board()

                else:  # This is a pawn move
                    print(turn + " plays " + move)
                    # If it is White's turn
                    if turn == "White":
                        # If this is a pawn promotion
                        if "=" in move:
                            rows[rank][file] = wQ
                            rows[rank + 1][file] = na
                            current_board()
                        # Else if this is not a pawn promotion
                        else:
                            # If this is not a capture
                            if "x" not in move:
                                # If there is a white pawn one rank below the ending square
                                if rows[rank + 1][file] == wP:
                                    rows[rank][file] = rows[rank + 1][file]
                                    rows[rank + 1][file] = na
                                    current_board()
                                # Else if there is a white pawn two ranks below the target square
                                else:
                                    rows[rank][file] = rows[rank + 2][file]
                                    rows[rank + 2][file] = na
                                    current_board()
                            # Else if this is a capture
                            else:
                                rows[rank][file] = rows[rank + 1][files[str(move[0])]]
                                rows[rank + 1][files[str(move[0])]] = na
                                current_board()
                    # Else if it is Black's turn
                    else:
                        # If this is a pawn promotion
                        if "=" in move:
                            rows[rank][file] = bQ
                            rows[rank - 1][file] = na
                            current_board()
                        # Else if this is not a pawn promotion
                        else:
                            # If this is not a capture
                            if "x" not in move:
                                if rows[rank - 1][file] == bP:
                                    rows[rank][file] = rows[rank - 1][file]
                                    rows[rank - 1][file] = na
                                    current_board()
                                else:
                                    rows[rank][file] = rows[rank - 2][file]
                                    rows[rank - 2][file] = na
                                    current_board()
                            # Else if this is a capture
                            else:
                                rows[rank][file] = rows[rank - 1][files[str(move[0])]]
                                rows[rank - 1][files[str(move[0])]] = na
                                current_board()

                if turn == "White":
                    turn = "Black"
                elif turn == "Black":
                    turn = "White"


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
