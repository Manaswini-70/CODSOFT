import math

def print_board(board):
    for row in board:
        print("|".join(row))
    print()

def check_winner(board):
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i]==board[1][i]==board[2][i] and board[0][i] != " ":
            return board[0][i]
    if board[0][0]==board[1][1]==board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2]==board[1][1]==board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O": return 1
    elif winner == "X": return -1
    elif all(cell != " " for row in board for cell in row): return 0
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth+1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth+1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    move = None
    best_score = -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = [[" "]*3 for _ in range(3)]
    print("Tic Tac Toe: You are X, AI is O")
    while True:
        print_board(board)
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if board[row][col] != " ":
            print("Invalid move, try again.")
            continue
        board[row][col] = "X"
        if check_winner(board):
            print_board(board)
            print("You win!")
            break
        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("It's a draw!")
            break
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = "O"
        if check_winner(board):
            print_board(board)
            print("AI wins!")
            break

play_game()
