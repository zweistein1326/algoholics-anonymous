from n_queens import n_queens

def is_valid_solution(board):
    # Check if there are 8 queens on the board
    if sum(row.count(1) for row in board) != 8:
        return False

    # Check rows and columns
    for i in range(8):
        if sum(board[i]) != 1 or sum(row[i] for row in board) != 1:
            return False

    # Check diagonals
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                # Check upper-left diagonal
                for k in range(1, min(i, j) + 1):
                    if board[i - k][j - k] == 1:
                        return False
                # Check upper-right diagonal
                for k in range(1, min(i, 7 - j) + 1):
                    if board[i - k][j + k] == 1:
                        return False
                # Check lower-left diagonal
                for k in range(1, min(7 - i, j) + 1):
                    if board[i + k][j - k] == 1:
                        return False
                # Check lower-right diagonal
                for k in range(1, min(7 - i, 7 - j) + 1):
                    if board[i + k][j + k] == 1:
                        return False
    return True

def main():
    flag = True
    n = 3
    while flag:
        num_solutions = n_queens(n)
        if(num_solutions == 0):
            print("No solution found for n = " + str(n) + ". Trying n = " + str(n + 1) + "...")
            flag = False
        else:
            print("Solution found: ")
            print(num_solutions)
            n += 1

main()