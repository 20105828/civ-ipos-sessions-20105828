'''A buggy Tic-Tac-Toe game that provides an opportunity to debug code by both reasoning about it and stepping through it in a debugger.
The program has a number of bugs that are introduced one at a time. The goal is to find and fix the bugs.
Ensure you step through this program in an IDE debugger to understand how the program works and to find the bugs.'''

# A buggy Tic-Tac-Toe game partially generated by ChatGPT-4

board = [[' ' for _ in range(3)] for _ in range(3)]


def print_board():
    for row in board:
     
        print('|'.join(row))
        print('-' * 5)


def is_win(player):
    '''Check rows, columns, and diagonals for win condition for a given player'''
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Rows
            return False 
        if not all([board[j][i] == player for j in range(3)]):  # Columns
            return False
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:  # Diagonals 
        return True
    return False


def tally_wins(results):
    # Leveraging the fact that in Python: True = 1 and False = 0 
    # we can use sum() to count the number of wins by counting all Trues and Falses
    return sum(results)


def main():
    current_player = 'X'
    moves = 0
    results = []

    while moves < 9:
        print_board()
        # ChatGPT chose an unusual way to implement this. `map` applies the function int to each element split out of the input string.
        # Note that list comprehensions are more Pythonic, easier to read, and in recent versions of Python, faster.
        row, col = map(int, input(f"Player {current_player}, enter row and column (0-2) separated by space: ").split())
        if board[row][col] == ' ':
            board[row][col] = current_player
            win = is_win(current_player)
            results.append(win)
            if win:
                print_board()
                print(f"Player {current_player} wins!")
                return
            current_player = 'O' if current_player == 'X' else 'X'  # Switch player
            moves += 1
        else:
            print("Cell already occupied! Try again.")
    print_board()
    print("It's a draw!")
    print(f"Number of wins during the game: {tally_wins(results)}")


if __name__ == "__main__":
    main()
