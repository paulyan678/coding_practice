class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def recurse(cur_comb, start):
            if len(cur_comb) == k:
                res.append(cur_comb)
                return
            for i in range(start, n + 1):
                recurse(cur_comb + [i], i + 1)
        recurse([], 1)
        return res