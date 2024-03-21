def n_queens(n):
    board = [-1] * n
    return n_queens_helper(board, 0)

# This function finds the number of solutions for the n-queens problem
def n_queens_helper(board, row):
    