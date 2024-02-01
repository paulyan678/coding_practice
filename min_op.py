import math

def min_op(n):
    if n == 1:
        return 0
    dp = [0] * (n+1)
    for even_num in range(2, n + 1, 2):
        dp[even_num] = math.log2(even_num)
    
    for odd_num in range(3, n + 1, 2):
        if odd_num < n:
            dp[odd_num] = min(dp[odd_num - 1], dp[odd_num + 1]) + 1
        else:
            dp[odd_num] = dp[odd_num - 1] + 1
    return dp[-1]

min_op(10)