class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        n = len(s)
        
        def backtract(i, cur_ans):
            if i >= n:
                res.append(cur_ans[1:])
            
            for j in range(i, n):
                if s[i:j+1] in wordDict:
                    backtract(j+1, cur_ans + " " + s[i:j+1])
        backtract(0, "")
        return res