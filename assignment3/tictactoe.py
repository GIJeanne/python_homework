#Task 6: More on Classes
class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Board:
    valid_moves = ["upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", "lower right"]

    def __init__(self):
        self.board_array = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.turn = "X"

    def __str__(self):
        lines = []
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)

    def move(self, move_string):
        if not move_string in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3  # row
        column = move_index % 3  # column
        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")
        self.board_array[row][column] = self.turn
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def whats_next(self):
        # Check for a win first, so a winning move that fills the board
        # is reported as a win rather than a Cat's Game.
        win = False
        for i in range(3):  # check rows
            if self.board_array[i][0] != " ":
                if self.board_array[i][0] == self.board_array[i][1] and self.board_array[i][1] == self.board_array[i][2]:
                    win = True
                    break
        if not win:
            for i in range(3):  # check columns
                if self.board_array[0][i] != " ":
                    if self.board_array[0][i] == self.board_array[1][i] and self.board_array[1][i] == self.board_array[2][i]:
                        win = True
                        break
        if not win:
            if self.board_array[1][1] != " ":  # check diagonals
                if self.board_array[0][0] == self.board_array[1][1] and self.board_array[2][2] == self.board_array[1][1]:
                    win = True
                if self.board_array[0][2] == self.board_array[1][1] and self.board_array[2][0] == self.board_array[1][1]:
                    win = True
        if win:
            # The turn has already flipped after the winning move.
            if self.turn == "O":
                return (True, "X wins!")
            else:
                return (True, "O wins!")

        cat = all(cell != " " for row in self.board_array for cell in row)
        if cat:
            return (True, "Cat's Game.")

        if self.turn == "X":
            return (False, "X's turn.")
        else:
            return (False, "O's turn.")


if __name__ == "__main__":
    board = Board()
    print("Tic-Tac-Toe. Valid moves: " + ", ".join(Board.valid_moves))
    print(board)

    game_over = False
    while not game_over:
        move_string = input(f"{board.turn}, enter your move: ").strip().lower()
        try:
            board.move(move_string)
        except TictactoeException as e:
            print(e.message)
            print("Try again.")
            continue
        print(board)
        game_over, message = board.whats_next()
        print(message)