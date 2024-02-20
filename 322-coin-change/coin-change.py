class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                reminder = i - coin
                if reminder < 0 or dp[reminder] == -1:
                    continue
                if dp[i] == -1:
                    dp[i] = dp[reminder] + 1
                else:
                    dp[i] = min(dp[reminder] + 1, dp[i])
        return dp[-1]
                
        