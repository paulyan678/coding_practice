def maximalSquare(matrix):
    dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        dp[i][0] = matrix[i][0]
        if '1' == dp[i][0]:
            max_sz = 1
    dp[0][:] = matrix[0][:]

    if '1' in dp[0]:
        max_sz = 1


    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if int(matrix[i][j]) == 0:
                dp[i][j] = 0
            else:
                cur_sz = min(int(dp[i][j-1]), int(dp[i-1][j-1]), int(dp[i-1][j])) + 1
                max_sz = cur_sz if cur_sz > max_sz else max_sz
                dp[i][j] = cur_sz
    return max_sz*max_sz

maximalSquare([["0"],["1"]])