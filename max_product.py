def integerBreak(n):
    dp = [1] * (n+1)
    for cur_num in range(2, n+1):
        for j in range(1, cur_num):
            dp[cur_num] = max(dp[cur_num], j*dp[cur_num-j], j*(cur_num-j))
    return dp[-1]

for i in range(2, 12):
    print(f'{i}: {integerBreak(i)}')