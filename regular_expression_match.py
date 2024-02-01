def isMatch(s, p):
    m = len(s)
    n = len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    
    for i in range(m+1):
        for j in range(1, n + 1):
            if p[j-1] == '*':
                # if any([dp[k][j-1] for k in range(i + 1)]):
                dp[i][j] = True
            elif p[j-1] == '.':
                dp[i][j] = dp[i-1][j-1]
            else:
                if p[j-1] == s[i-1] and i > 0:
                    dp[i][j] = dp[i-1][j-1]
    
    return dp[-1][-1]

print(isMatch('aab', 'c*a*b'))



