from functools import cmp_to_key


    
def maxEnvelopes(envelopes):
    def my_compare(a, b):
        if a[0] == b[0]:
            return b[1] - a[1]
        else:
            return a[0] - b[0]
    envelopes = sorted(envelopes, key=cmp_to_key(my_compare), reverse=True)
    print(envelopes)
    dp = [1]*len(envelopes)
    
    for i in range(1, len(envelopes)):
        for j in range(i):
            if envelopes[j][1] > envelopes[i][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(maxEnvelopes([[1,1],[1,1],[1,1]]))




        
