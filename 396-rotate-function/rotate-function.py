class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        s = sum(nums)
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[0] += i*nums[i]
        
        for i in range(1, len(nums)):
            dp[i] = dp[i-1] + s - len(nums)*nums[len(nums)-i]
        
        return max(dp)
        