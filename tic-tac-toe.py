from random import randrange

##for i in range(10):
##    print(randrange(8))

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print('''
+-------+-------+-------+
|       |       |       |
|   '''+board[0]+'''   |   '''+board[1]+'''   |   '''+board[2]+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+board[3]+'''   |   '''+board[4]+'''   |   '''+board[5]+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+board[6]+'''   |   '''+board[7]+'''   |   '''+board[8]+'''   |
|       |       |       |
+-------+-------+-------+
    
    
    
    ''')


def enter_move(board):
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.
    move = input("Enter you move: ")
    if move == board[int(move)-1] and (board[int(move)-1] != "O" or board[int(move)-1] != "X"):
        board[int(move)-1] = "O"
    else:
        print("block occupied")
        enter_move(board)



def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    
    pass


def victory_for(board, sign):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    if board[0]== board[1]== board[2]:
        print(sign + 'wins')
        return False
    if board[3]== board[4]== board[5]:
        print(sign + 'wins')
        return False
    if board[6]== board[7]== board[8]:
        print(sign + 'wins')
        return False
    if board[0]== board[3]== board[6]:
        print(sign + 'wins')
        return False
    if board[1]== board[4]== board[7]:
        print(sign + 'wins')
        return False
    if board[2]== board[5]== board[8]:
        print(sign + 'wins')
        return False
    if board[0]== board[4]== board[8]:
        print(sign + 'wins')
        return False
    if board[2]== board[4]== board[6]:
        print(sign + 'wins')
        return False        
    return True


def draw_move(board):
    # The function draws the computer's move and updates the board.
    drawing = True
    while drawing:
        move = randrange(0,9)
        print(board)
        print(move)
        if board[move] != 'X' and board[move] != 'O':
            board[move] = 'X'            
            drawing = False
            print("pc chose block: ", move+1)
            

board = ['1','2','3','4','X','6','7','8','9']
playing = True
display_board(board)
count = 0
while playing and count < 8:
    enter_move(board)
    display_board(board)
    playing = victory_for(board,"O")
    if not playing:
        break
    draw_move(board)
    display_board(board)
    playing = victory_for(board,"X")
    count+=2
    print('count', count)

if count == 8:
    print('tie')
    
print("done")
    
