class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def recurse(cur_list, start, cur_sum):
            if cur_sum == target:
                res.append(list(cur_list))  # Use list(cur_list) to create a copy
                return
            if cur_sum > target:
                return

            for i in range(start, len(candidates)):
                num = candidates[i]
                cur_list.append(num)
                recurse(cur_list, i , cur_sum + num)
                cur_list.pop()

        recurse([], 0, 0)
        return res
