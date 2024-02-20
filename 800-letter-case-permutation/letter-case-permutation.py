class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        n = len(s)
        def recurse(i, cur_str):
            if i == n:
                res.append(cur_str)
                return
            char = s[i]
            if char.isdigit():
                recurse(i + 1, cur_str + s[i])
            else:
                recurse(i + 1, cur_str + s[i].upper())
                recurse(i + 1, cur_str + s[i].lower())
        recurse(0, '')
        return res

        