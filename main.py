"""Declaration of variables"""
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
player1 = "X"
player2 = "O"
gturn = player1
isGameFinished = None

"""Functions declaration and realization"""


def make_move(turn):
    penalty_counter = 0
    print("Enter cell number from 0-9: ")
    print("0", "1", "2")
    print("3", "4", "5")
    print("6", "7", "8")
    a = int(input())
    # Check if chosen field is taken
    while board[a] != "-":
        print("Field is taken, please try another one: ")
        a = int(input())
        penalty_counter += 1
        if penalty_counter == 2:
            # And punish if player trying to prevent program to end by always choosing taken tile
            print("Player", turn, "disqualified")
            quit()
    if turn == player1:
        board[a] = "X"
        turn = player2
    elif turn == player2:
        board[a] = "O"
        turn = player1
    draw_board()
    return turn


def draw_board():
    # Function which displays current situation on board
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])


def check_for_win():
    # Function which checks if win conditions has been satisfied
    if board[0] == board[1] and board[1] == board[2] and board[2] != "-":
        print("Player", board[1], "wins ")
        return True
    elif board[3] == board[4] and board[4] == board[5] and board[5] != "-":
        print("Player", board[3], "wins ")
        return True
    elif board[6] == board[7] and board[7] == board[8] and board[8] != "-":
        print("Player", board[6], "wins ")
        return True
    elif board[0] == board[3] and board[3] == board[6] and board[6] != "-":
        print("Player", board[0], "wins ")
        return True
    elif board[1] == board[4] and board[4] == board[7] and board[7] != "-":
        print("Player", board[1], "wins ")
        return True
    elif board[2] == board[5] and board[5] == board[8] and board[8] != "-":
        print("Player", board[2], "wins ")
        return True
    elif board[0] == board[4] and board[4] == board[8] and board[8] != "-":
        print("Player", board[0], "wins ")
        return True
    elif board[6] == board[4] and board[4] == board[2] and board[2] != "-":
        print("Player", board[6], "wins ")
        return True
    else:
        return False


"""Main Body"""


draw_board()
for i in range(len(board)):
    gturn = make_move(gturn)
    isGameFinished = check_for_win()
    if isGameFinished:
        print("Game Over")
        break
if not isGameFinished:
    print("Draw")
