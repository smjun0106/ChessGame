size_board = 8
board = [] 
count = ' '

for row in range(size_board):
    column = []
    for col in range(size_board):
        column.append(count)    

    board.append(column)
 
# dictionary 
pieces = {
    1: '♙', 2: '♙', 3: '♙', 4:'♙', 5: '♙', 6: '♙', 7: '♙', 8: '♙',
    9: '♖', 10: '♘', 11: '♗', 12: '♕', 13: '♔', 14: '♗', 15: '♘', 16: '♖',
    17: '♟︎', 18: '♟︎', 19:'♟︎', 20: '♟︎', 21: '♟︎', 22: '♟︎', 23: '♟︎', 24: '♟︎', 
    25: '♜', 26: '♞', 27: '♝', 28:'♛', 29: '♚', 30: '♝', 31: '♞', 32: '♜',
}

pieces_type = {1: 'pawn', 2: 'rook', 3: 'queen', 4:'king', 5: 'knight', 6: 'bishop'}

piece_category = {
    1: 1, 2: 1, 3: 1, 4:1, 5: 1, 6: 1, 7: 1, 8: 1,
    9: 2, 10: 5, 11: 6, 12: 3, 13: 4, 14: 6, 15: 5, 16: 2,
    17: 1, 18: 1, 19:1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 
    25: 2, 26: 5, 27: 6, 28:3, 29: 4, 30: 6, 31: 5, 32: 2,
    }
 
alive_pieces = {key: True for key in range(1, 33)}
 
locations = {
    1: (6,0), 2: (6,1), 3: (6,2), 4: (6,3), 5: (6,4), 6: (6,5), 7: (6,6), 8: (6,7),
    9: (7,0), 10: (7,1), 11: (7,2), 12: (7,3), 13: (7,4), 14: (7,5), 15: (7,6), 16: (7,7),
    17: (1,0), 18: (1,1), 19: (1,2), 20: (1,3), 21: (1,4), 22: (1,5), 23: (1,6), 24: (1,7),
    25: (0,0), 26: (0,1), 27: (0,2), 28: (0,3), 29: (0,4), 30: (0,5), 31: (0,6), 32: (0,7),
} 

# global variable 
is_white_turn = True

def switch_turn():
    global is_white_turn

    if is_white_turn:
        is_white_turn = False
    else:
        is_white_turn = True

def switch_turn_pieces():
    if (is_white_turn and locations in range (1, 17)) or (not is_white_turn and locations not in range (1,17)):
        return True
    else:
        return False
    
def is_piece(row, col):
    for id, value in locations.items():
        if (row, col) == value:
            return id

    return False    

def remove_piece(piece):
    board[locations[piece][0]][locations[piece][1]] = '[]'
    locations[piece] = (int(-1), int(-1))

def check_for_killed_piece(row, col):
    killed_id = is_piece(row, col)
    if killed_id:
        remove_piece(killed_id)
        alive_pieces[killed_id] = False 
        return True
    return False
  
def move_piece(r, c): 
    locations[selected_piece] = (int(r), int(c))
  
def put_pieces(): 
    for p, v in pieces.items():  
        if alive_pieces[p] == True: 
            board[locations[p][0]][locations[p][1]] = pieces[p]

 
# Type a code for the rule for pawn 
# selected_piece = 13   
# move_piece(4, 3) 
put_pieces()
   
def print_board():
    for i in range(size_board):
        print(board[i])
    
    print_killed_pieces()

 
def print_killed_pieces():
    line_size = 50 

    killed_list = []
    for p, v in pieces.items():
        if alive_pieces[p] != True:
           killed_list.append(v) 
                    
    print(killed_list)
           
# Print board
print_board()

#=======================================================
def is_valid_move_knight(row, col):
    for i in range(-2,3):
        for j in range(-2,3): 
             if i != 0 and j != 0 and abs(i) != abs(j):
                if row == locations[selected_piece][0] + i and col == locations[selected_piece][1] + j:
                    return True
    return False
  
#=======================================================
def is_valid_move_pawn(row, col):    
    if locations[selected_piece][0] == 6:
        if (row == locations[selected_piece][0] - 1 and col == locations[selected_piece][1]) \
            or (row == locations[selected_piece][0] - 2 and col == locations[selected_piece][1]):
            return is_piece(row, col) == False  
    elif row == locations[selected_piece][0] - 1 and col == locations[selected_piece][1]:
            return is_piece(row, col) == False 
    
    if (row == locations[selected_piece][0] - 1 and col == locations[selected_piece][1] + 1) or \
        (row == locations[selected_piece][0] - 1 and col == locations[selected_piece][1] - 1):
        if is_piece(row, col):
            return not check_same_team(selected_piece, is_piece(row, col))
        else:
            return False  # destination is empty
 
    return False 
    
def check_same_team(id1, id2):
    if id1 in range(1, 17) and id2 in range(1, 17):
        return True
    if id1 in range(16, 33) and id2 in range(16, 33):
        return True     
    
    return False

#=======================================================
# bishop
def is_valid_move_bishop(row, col):
    current_row, current_col = locations[selected_piece]
    # check if move is diagonal
    if abs(row - current_row) != abs(col - current_col):
        return False
        
    # check if path is clear
    row_step = 1 if row > current_row else -1
    col_step = 1 if col > current_col else -1
    i = current_row + row_step
    j = current_col + col_step
    while i != row and j != col:
        if is_piece(i, j):
            return False  # path is not clear
        i += row_step
        j += col_step
    
    # check if destination is empty or occupied by an enemy piece
    if is_piece(row, col):
        return not check_same_team(selected_piece, is_piece(row, col))
    else:
        return True  # destination is empty

#======================================================= 
# rook
def is_valid_move_rook(row, col):
    current_row, current_col = locations[selected_piece]
    
    # Check if the move is vertical or horizontal
    if row == current_row or col == current_col:
        
        # Check if there are any pieces blocking the way
        if row == current_row:
            direction = 1 if col > current_col else -1
            for c in range(current_col + direction, col, direction):
                if is_piece(row, c):
                    return False
        else:
            direction = 1 if row > current_row else -1
            for r in range(current_row + direction, row, direction):
                if is_piece(r, col):
                    return False
                            
        # check if the destination is occupied by an opponent's piece
        if is_piece(row, col):
            return not check_same_team(selected_piece, is_piece(row, col))
        else:
            return True  # destination is empty
    
    return False

#=======================================================  
# queen
def is_valid_move_queen(row, col):
    # check if the selected piece is a queen
    if piece_category[selected_piece] != 3:
        return False
    
    # check if the destination is within the board
    if not (0 <= row < size_board and 0 <= col < size_board):
        return False
    
    # get the current position of the selected piece
    current_row, current_col = locations[selected_piece]
    
    # check if the destination is the same as the current position
    if (row, col) == (current_row, current_col):
        return False
    
    # check if the move is horizontal, vertical, or diagonal
    if row != current_row and col != current_col and abs(row - current_row) != abs(col - current_col):
        return False
    
    # check if there are any pieces in the way
    if row == current_row:
        # horizontal move
        start, end = min(current_col, col), max(current_col, col)
        for i in range(start + 1, end):
            if is_piece(row, i):
                return False
    elif col == current_col:
        # vertical move
        start, end = min(current_row, row), max(current_row, row)
        for i in range(start + 1, end):
            if is_piece(i, col):
                return False
    else:
        # diagonal move
        dx, dy = 1 if row > current_row else -1, 1 if col > current_col else -1
        i, j = current_row + dx, current_col + dy
        while (i, j) != (row, col):
            if is_piece(i, j):
                return False
            i += dx
            j += dy
    
    # check if the destination is occupied by an opponent's piece
    if is_piece(row, col):
        return not check_same_team(selected_piece, is_piece(row, col))
    else:
        return True  # destination is empty

    # all checks passed, the move is valid
    return True

#======================================================= 
# king
def is_valid_move_king(row, col):
    # check if the selected piece is a king
    if piece_category[selected_piece] != 4:
        return False
    
    # check if the destination is within the board
    if not (0 <= row < size_board and 0 <= col < size_board):
        return False
    
    # get the current position of the selected piece
    current_row, current_col = locations[selected_piece]
    
    # check if the destination is the same as the current position
    if (row, col) == (current_row, current_col):
        return False
    
    # check if the move is horizontal, vertical, or diagonal
    if row != current_row and col != current_col and abs(row - current_row) != abs(col - current_col):
        return False

    diff_row, diff_col = abs(current_row - row), abs(current_col - col)
    if diff_row > 1 or diff_col > 1:   
        return False      

    # check if the destination is occupied by an opponent's piece
    if is_piece(row, col):
        return not check_same_team(selected_piece, is_piece(row, col))
    else:
        return True  # destination is empty

    # all checks passed, the move is valid
    return True

#=======================================================================
#  Main 
def repeat_code():
    global selected_piece  
    
    print('current turn:', 'white' if is_white_turn else 'black')

    selected_piece = int(input('choose piece = '))
    row = int(input('row = '))
    col = int(input('col = '))
    
    pieces_str = pieces_type[piece_category[selected_piece]] 

    match pieces_str:
        case 'knight':
            func = is_valid_move_knight
        case 'pawn':
            func = is_valid_move_pawn
        case 'bishop':
            func = is_valid_move_bishop
        case 'rook':
            func = is_valid_move_rook
        case 'queen':
            func = is_valid_move_queen
        case 'king':
            func = is_valid_move_king
 
    if func(row, col):
        if switch_turn_pieces():
            print ('Invalid move, please try again')
            repeat_code()
        else:
            if check_for_killed_piece(row, col):
                print('Piece killed!')
            remove_piece(selected_piece)
            move_piece(row, col)
            put_pieces()
            print_board()
            switch_turn()
            repeat_code()
    else:
        print('Invalid move, please try again')
        repeat_code()

repeat_code()
