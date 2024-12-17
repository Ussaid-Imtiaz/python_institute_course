from random import choice

board = [[1,2,3],[4,"X",6],[7,8,9]]

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(f"""
+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+
""")


def enter_move(board):
    # Get a valid move from the user
    while True:
        try:
            user_move = int(input("Enter your move (1-9): "))
            if user_move < 1 or user_move > 9:
                raise ValueError
            row, col = (user_move - 1) // 3, (user_move - 1) % 3
            if board[row][col] not in ['X', 'O']:
                board[row][col] = 'O'
                break
            else:
                print("This position is already taken. Choose another.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")    


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    empty_sqaures = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 'X' and board[i][j] != 'O':
                empty_sqaures.append((i,j))
    return empty_sqaures


def victory_for(board):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    # if make_list_of_free_fields(board) == []:
    #     print("Its a Tie")
    if (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") or \
        (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") or \
        (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X") or \
        (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X") or \
        (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X") or \
        (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X") or \
        (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or \
        (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X"):
        return "Computer"
    elif (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O") or \
        (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O") or \
        (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O") or \
        (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O") or \
        (board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O") or \
        (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O") or \
        (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") or \
        (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"):
        return "Player"
    


def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_squares = make_list_of_free_fields(board)
    if free_squares:
        row,col = choice(free_squares)
        print(f"Computer move is ({row+1},{col+1})")
        board[row][col] = "X"
    
def play_game():
    turn = "Player"
    while True:
        display_board(board)

        if turn == "Player":
            enter_move(board)
        else:
            draw_move(board)
        
        winner = victory_for(board)
        if winner:
            print(f'{winner} won')
            break

        if not make_list_of_free_fields(board):
            print("Its a Tie")
            break

        if turn == "Player":
            turn = "Computer"
        else:
            turn = "Player"

      
play_game()