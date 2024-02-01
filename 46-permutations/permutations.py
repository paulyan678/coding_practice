class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def recurse(permutation, availble_nums):
            if len(availble_nums) == 0:
                res.append(permutation)
                return
            for i, num in enumerate(availble_nums):
                recurse(permutation + [num], availble_nums[:i] + availble_nums[i+1:])
        recurse([], nums)
        return res
        