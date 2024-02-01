import math

def n_queens_recurse(board, n):
    count  = 0
    if n == 0:
        return 1
    
    for i in range(len(board)):
        for j in range(len(board)):
            copy_board = [row[:] for row in board]
            if board[i][j]:
                for k in range(len(board)):
                    copy_board[k][j] = False

                    copy_board[i][k] = False

                    if i+k < len(board) and j+k < len(board):
                        copy_board[i+k][j+k] = False
                    if i-k >= 0 and j-k >= 0:
                        copy_board[i-k][j-k] = False
                    if i+k < len(board) and j-k >= 0:
                        copy_board[i+k][j-k] = False
                    if i-k >= 0 and j+k < len(board):
                        copy_board[i-k][j+k] = False

                
                count += n_queens_recurse(copy_board, n-1)
    return count

def n_queens(size, num_queens):
    board = [[True]*size for _ in range(size)]
    return n_queens_recurse(board, num_queens) / math.factorial(num_queens)

print(n_queens(6, 6))
