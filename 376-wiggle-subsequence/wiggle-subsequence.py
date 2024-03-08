class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp_p = [1] * n
        dp_n = [1] * n
        for i in range(1, n):
            for j in range(i):
            # rise positive
                if nums[i] > nums[j]:
                    dp_p[i] = max(dp_p[i], 1 + dp_n[j])
                elif nums[i] < nums[j]:
                    dp_n[i] = max(dp_n[i], 1 + dp_p[j])
        return max(max(dp_p), max(dp_n))

        