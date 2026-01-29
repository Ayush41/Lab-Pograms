import random

board = [' ' for _ in range(9)]

def display_board():
    print()
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
    print()

def check_winner(player):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_draw():
    return ' ' not in board

def player_move():
    while True:
        move = int(input("Enter your move (1-9): ")) - 1
        if 0 <= move < 9 and board[move] == ' ':
            board[move] = 'X'
            break
        else:
            print("Invalid move. Try again.")

def computer_move():
    available=[]
    for i in range(9):
        if board[i]==' ':
            available.append(i)
    move = random.choice(available)
    board[move] = 'O'
    print("Computer played at position", move + 1)

print("Tic-Tac-Toe (Player vs Computer)")
print("Game continues till someone wins or the match is a draw.")
display_board()

while True:
    player_move()
    display_board()

    if check_winner('X'):
        print("Player wins!")
        break
    if is_draw():
        print("Match Draw!")
        break

    computer_move()
    display_board()

    if check_winner('O'):
        print(" Computer wins!")
        break
    if is_draw():
        print("Match Draw!")
        break