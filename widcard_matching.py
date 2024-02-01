
'''
      _  _    s _
   | 
p |


'''

def wildCardMatching(s, p):
    dp = [[False]*(len(s) + 1) for _ in range(len(p) + 1)]
    dp[0][0] = True

    for j in range(1, len(p)+1):
        if p[j-1] == '*':
            dp[j][0] = dp[j-1][0]
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if p[i - 1] == '*':
                dp[i][j] = dp[i-1][j] or any(dp[i][:j])
            if p[i - 1] == '?' or p[i - 1] == s[j - 1]:
                dp[i][j] = dp[i-1][j-1]
    return dp[-1][-1]

print(wildCardMatching('', '*********'))
