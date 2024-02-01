def n_queens(n):
    results = []
    board = [[False]*n for _ in range(n)]
    queen_placement = [None for _ in range(n)]
    stack = [(i, j, 0) for i in range(n) for j in range(n)]

    def is_valid_queen_placement(row, col):
        if any(board[row][j] for j in range(n)) or any(board[i][col] for i in range(n)):
            return False
        
        # check diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j]:
                return False
            i -= 1
            j -= 1
        
        i, j = row, col
        while i < n and j < n:
            if board[i][j]:
                return False
            i += 1
            j += 1

        i, j = row, col

        while i >= 0 and j < n:
            if board[i][j]:
                return False
            i -= 1
            j += 1
        
        i, j = row, col
        while i < n and j >= 0:
            if board[i][j]:
                return False
            i += 1
            j -= 1
        
        return True

    while len(stack) > 0:
        i, j, cur_queen_num = stack.pop()
        for future_queen_placement in range(cur_queen_num, n):
            if queen_placement[future_queen_placement] is not None:
                board[queen_placement[future_queen_placement][0]][queen_placement[future_queen_placement][1]] = False
            queen_placement[future_queen_placement] = None


        queen_placement[cur_queen_num] = (i, j)
        board[i][j] = True

        if cur_queen_num == n - 1:
            temp = [['.']*n for _ in range(n)]
            for i, j in queen_placement:
                temp[i][j] = 'Q'
            temp = [''.join(row) for row in temp]
            if temp not in results:
                results.append(temp)
            continue
        
        for i in range(n):
            for j in range(n):
                if is_valid_queen_placement(i, j):
                    stack.append((i, j, cur_queen_num+1))
        
    return results

print(len(n_queens(6)))
    



    



