class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
            
        if len(nums) == 1:
            return nums[0]
        def helper(houses):
            dp = [0]*(len(houses) + 2)
            for i in range(2, len(houses) + 2):
                dp[i] = max(dp[i-1], dp[i-2] + houses[i-2])
            return dp[-1]
        return max(helper(nums[1:]), helper(nums[:-1]))