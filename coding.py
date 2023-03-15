# Homework: create the rook rule (check our pieces and enemy pieces, then move)
size_board = 8
board = [] 
count = '[]'

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
 

# Type a code for the rule for pawn 
seleced_piece = 10  
 
def remove_piece(piece):
    board[locations[piece][0]][locations[piece][1]] = '[]'

def check_for_killed_piece(row, col):
    killed_id = is_piece(row, col)
    if killed_id:
        remove_piece(killed_id)
        alive_pieces[killed_id] = False 
        return True
    return False
  
def move_piece(r, c): 
    locations[seleced_piece] = (int(r), int(c))
  
def put_pieces(): 
    for p, v in pieces.items():  
        if alive_pieces[p] == True: 
            board[locations[p][0]][locations[p][1]] = pieces[p]

move_piece(3, 4)
 
put_pieces()
   
def print_board():
    for i in range(size_board):
        print(board[i])
    
    print_killed_pieces()

# ['1','2']
def print_killed_pieces():
    line_size = 50 

    killed_list = []
    for p, v in pieces.items():
        if alive_pieces[p] != True:
           killed_list.append(v) 
                    
    print(killed_list)
           
# Print board
print_board()
 
def is_valid_move_knight(row, col):
    for i in range(-2,3):
        for j in range(-2,3): 
             if i != 0 and j != 0 and abs(i) != abs(j):
                if row == locations[seleced_piece][0] + i and col == locations[seleced_piece][1] + j:
                    return True
    return False

def check_enemy(row, col):
    if row == locations[seleced_piece][0] - 1 and (col == locations[seleced_piece][1] + 1 or col == locations[seleced_piece][1] - 1):
        
        # check for enemy piece
        killed_id = is_piece(row, col)
        if killed_id and killed_id not in range(1, 17):
            remove_piece(killed_id)
            alive_pieces[killed_id] = False 
            return True

def is_valid_move_pawn(row, col):    
    if locations[seleced_piece][0] == 6:
        if (row == locations[seleced_piece][0] - 1 and col == locations[seleced_piece][1]) or (row == locations[seleced_piece][0] - 2 and col == locations[seleced_piece][1]):
            return True
    else:   
        if row == locations[seleced_piece][0] - 1 and col == locations[seleced_piece][1]:
            return True
        
    return check_enemy(row, col)
 
def is_piece(row, col):
    for id, value in locations.items():
        if (row, col) == value:
            return id
    
    return False    
    
def repeat_code():
    global seleced_piece
    
    seleced_piece = int(input('choose piece = '))
    row = int(input('row = '))
    col = int(input('col = '))
    
    pieces_str = pieces_type[piece_category[seleced_piece]] 

    match pieces_str:
        case 'knight':
            func = is_valid_move_knight
        case 'pawn':
            func = is_valid_move_pawn
        case 'rook':
            pass
 
    if func(row, col):
        if check_for_killed_piece(row, col):
            print('Piece killed!')
        remove_piece(seleced_piece)
        move_piece(row, col)
        put_pieces()
        print_board()
        repeat_code()
    else:
        print('Invalid move, please try again')
        repeat_code()

repeat_code()

----------------------------------------------------------------------------

(still need help with writing the rule)

size_board = 8
board = [] 
count = '[]'

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
 

# Type a code for the rule for pawn 
seleced_piece = 10  
 
def remove_piece(piece):
    board[locations[piece][0]][locations[piece][1]] = '[]'

def check_for_killed_piece(row, col):
    killed_id = is_piece(row, col)
    if killed_id:
        remove_piece(killed_id)
        alive_pieces[killed_id] = False 
        return True
    return False
  
def move_piece(r, c): 
    locations[seleced_piece] = (int(r), int(c))
  
def put_pieces(): 
    for p, v in pieces.items():  
        if alive_pieces[p] == True: 
            board[locations[p][0]][locations[p][1]] = pieces[p]

move_piece(3, 4)
 
put_pieces()
   
def print_board():
    for i in range(size_board):
        print(board[i])
    
    print_killed_pieces()

# ['1','2']
def print_killed_pieces():
    line_size = 50 

    killed_list = []
    for p, v in pieces.items():
        if alive_pieces[p] != True:
           killed_list.append(v) 
                    
    print(killed_list)
           
# Print board
print_board()
 
def is_valid_move_knight(row, col):
    for i in range(-2,3):
        for j in range(-2,3): 
             if i != 0 and j != 0 and abs(i) != abs(j):
                if row == locations[seleced_piece][0] + i and col == locations[seleced_piece][1] + j:
                    return True
    return False

def check_enemy(row, col):
    if row == locations[seleced_piece][0] - 1 and (col == locations[seleced_piece][1] + 1 or col == locations[seleced_piece][1] - 1):
        
        # check for enemy piece
        killed_id = is_piece(row, col)
        if killed_id and killed_id not in range(1, 17):
            remove_piece(killed_id)
            alive_pieces[killed_id] = False 
            return True

def is_valid_move_pawn(row, col):    
    if locations[seleced_piece][0] == 6:
        if (row == locations[seleced_piece][0] - 1 and col == locations[seleced_piece][1]) or (row == locations[seleced_piece][0] - 2 and col == locations[seleced_piece][1]):
            return True
    else:   
        if row == locations[seleced_piece][0] - 1 and col == locations[seleced_piece][1]:
            return True
        
    return check_enemy(row, col)
    
def is_valid_move_bishop(row, col):
    current_row, current_col = locations[seleced_piece]
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
        return piece_category[seleced_piece] != piece_category[is_piece(row, col)]
    else:
        return True  # destination is empty

def is_piece(row, col):
    for id, value in locations.items():
        if (row, col) == value:
            return id
    
    return False    
    
def repeat_code():
    global seleced_piece
    
    seleced_piece = int(input('choose piece = '))
    row = int(input('row = '))
    col = int(input('col = '))
    
    pieces_str = pieces_type[piece_category[seleced_piece]] 

    match pieces_str:
        case 'knight':
            func = is_valid_move_knight
        case 'pawn':
            func = is_valid_move_pawn
        case 'bishop':
            func = is_valid_move_bishop
        case 'rook':
            pass
        case 'queen':
            pass
        case 'king':
            pass
 
    if func(row, col):
        if check_for_killed_piece(row, col):
            print('Piece killed!')
        remove_piece(seleced_piece)
        move_piece(row, col)
        put_pieces()
        print_board()
        repeat_code()
    else:
        print('Invalid move, please try again')
        repeat_code()

repeat_code()
