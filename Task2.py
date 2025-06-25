# Task 2: Tic Tac Toe with Unbeatable AI (Minimax)
import math

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board):
    # Check rows, columns, diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    for row in board:
        if ' ' in row:
            return None  # Game still going
    return 'Tie'  # No empty spots

def minimax(board, depth, is_max):
    result = check_winner(board)
    if result == 'O':
        return 1
    elif result == 'X':
        return -1
    elif result == 'Tie':
        return 0

    if is_max:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe (You = X, AI = O)")
    print_board(board)

    while True:
        # Player move
        while True:
            try:
                row = int(input("Enter your move row (0-2): "))
                col = int(input("Enter your move column (0-2): "))
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    break
                else:
                    print("Cell is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter numbers between 0 and 2.")

        print_board(board)

        if check_winner(board):
            break

        print("AI is making a move...")
        i, j = best_move(board)
        board[i][j] = 'O'

        print_board(board)

        if check_winner(board):
            break

    winner = check_winner(board)
    if winner == 'Tie':
        print("It's a tie! 🤝")
    else:
        print(f"{'You win! 🎉' if winner == 'X' else 'AI wins! 🤖'}")

if __name__ == "__main__":
    play_game()
