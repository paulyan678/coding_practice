class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = {}
        nums = [1] + nums + [1]  # Padding to handle the edge balloons

        def recurse(i, j):
            key = (i, j)
            if key in memo:
                return memo[key]
            if i > j:  # Corrected base case: there's no balloon left to burst
                return 0
            
            res = 0
            for k in range(i, j + 1):
                # Calculate the value gained by bursting the kth balloon last in this range
                # and recursively calculate the value for the left and right subranges.
                # There's no need to handle k == i or k == j separately.
                left = recurse(i, k - 1)
                right = recurse(k + 1, j)
                res = max(res, nums[k] * nums[i - 1] * nums[j + 1] + left + right)
            
            memo[key] = res
            return res

        # Adjusted the range to exclude the padding
        return recurse(1, len(nums) - 2)