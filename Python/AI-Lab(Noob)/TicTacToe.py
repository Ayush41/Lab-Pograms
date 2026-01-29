class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def print_board(self):
        print("\n")
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            if i < 6:
                print("--+---+--")
        print("\n")

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            return True
        return False

    def check_winner(self):
        combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for combo in combos:
            if all(self.board[i] == self.current_player for i in combo):
                return True
        return False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def play(self):
        print("Welcome to Tic Tac Toe!")
        self.print_board()

        for turn in range(9):
            try:
                move = int(input(f"Player {self.current_player}, enter your move (1-9): ")) - 1
                if move < 0 or move > 8 or not self.make_move(move):
                    print("Invalid move. Try again.")
                    continue

                self.print_board()

                if self.check_winner():
                    print(f"🎉 Player {self.current_player} wins!")
                    return

                self.switch_player()

            except ValueError:
                print("Please enter a valid number between 1 and 9.")

        print("It's a draw!")

# Run the game
game = TicTacToe()
game.play()

