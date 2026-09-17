import math


# ============================================================
# AI TIC-TAC-TOE USING MINIMAX
# Fundamentals of AI and ML
# ============================================================


HUMAN = "X"
AI = "O"


# ------------------------------------------------------------
# DISPLAY BOARD
# ------------------------------------------------------------

def display_board(board):
    print()
    print("       TIC-TAC-TOE")
    print()

    for i in range(3):
        print("       " + " | ".join(board[i * 3:(i + 1) * 3]))

        if i < 2:
            print("      ---+---+---")

    print()


# ------------------------------------------------------------
# CHECK WINNER
# ------------------------------------------------------------

def check_winner(board):

    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:

        if board[a] == board[b] == board[c]:
            if board[a] != " ":
                return board[a]

    return None


# ------------------------------------------------------------
# CHECK DRAW
# ------------------------------------------------------------

def is_draw(board):
    return " " not in board and check_winner(board) is None


# ------------------------------------------------------------
# GET AVAILABLE MOVES
# ------------------------------------------------------------

def get_available_moves(board):

    return [
        i for i in range(9)
        if board[i] == " "
    ]


# ------------------------------------------------------------
# MINIMAX ALGORITHM
# ------------------------------------------------------------

def minimax(board, depth, maximizing):

    winner = check_winner(board)

    # AI wins
    if winner == AI:
        return 10 - depth

    # Human wins
    if winner == HUMAN:
        return depth - 10

    # Draw
    if is_draw(board):
        return 0

    # AI's turn
    if maximizing:

        best_score = -math.inf

        for move in get_available_moves(board):

            board[move] = AI

            score = minimax(
                board,
                depth + 1,
                False
            )

            board[move] = " "

            best_score = max(
                best_score,
                score
            )

        return best_score

    # Human's turn
    else:

        best_score = math.inf

        for move in get_available_moves(board):

            board[move] = HUMAN

            score = minimax(
                board,
                depth + 1,
                True
            )

            board[move] = " "

            best_score = min(
                best_score,
                score
            )

        return best_score


# ------------------------------------------------------------
# FIND BEST AI MOVE
# ------------------------------------------------------------

def find_best_move(board):

    best_score = -math.inf
    best_move = None

    for move in get_available_moves(board):

        board[move] = AI

        score = minimax(
            board,
            0,
            False
        )

        board[move] = " "

        if score > best_score:

            best_score = score
            best_move = move

    return best_move


# ------------------------------------------------------------
# HUMAN MOVE
# ------------------------------------------------------------

def human_move(board):

    while True:

        try:

            move = int(
                input("Enter your move (1-9): ")
            )

            move -= 1

            if move < 0 or move > 8:
                print("Please choose a number from 1 to 9.")
                continue

            if board[move] != " ":
                print("That position is already occupied.")
                continue

            board[move] = HUMAN
            break

        except ValueError:

            print("Please enter a valid number.")


# ------------------------------------------------------------
# PLAY GAME
# ------------------------------------------------------------

def play_game():

    board = [" "] * 9

    print()
    print("=" * 50)
    print("        AI TIC-TAC-TOE")
    print("        MINIMAX AI")
    print("=" * 50)

    print()
    print("You are X")
    print("AI is O")

    print()
    print("Board positions:")

    print("       1 | 2 | 3")
    print("      ---+---+---")
    print("       4 | 5 | 6")
    print("      ---+---+---")
    print("       7 | 8 | 9")

    print()

    while True:

        # Human turn
        display_board(board)

        human_move(board)

        winner = check_winner(board)

        if winner == HUMAN:

            display_board(board)

            print("You win!")

            break

        if is_draw(board):

            display_board(board)

            print("The game is a draw!")

            break

        # AI turn
        print()
        print("AI is thinking...")

        ai_move = find_best_move(board)

        board[ai_move] = AI

        winner = check_winner(board)

        if winner == AI:

            display_board(board)

            print("AI wins!")

            break

        if is_draw(board):

            display_board(board)

            print("The game is a draw!")

            break


# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------

def main():

    while True:

        print()
        print("=" * 50)
        print("       AI TIC-TAC-TOE PROJECT")
        print("=" * 50)

        print()
        print("1. Play against AI")
        print("2. Exit")

        print()

        choice = input("Enter your choice: ")

        if choice == "1":

            play_game()

            again = input(
                "Play again? (y/n): "
            ).lower()

            if again != "y":
                print("Thank you for playing!")
                break

        elif choice == "2":

            print("Thank you for using AI Tic-Tac-Toe!")
            break

        else:

            print("Invalid choice. Please try again.")


# ------------------------------------------------------------
# START PROGRAM
# ------------------------------------------------------------

if __name__ == "__main__":
    main()