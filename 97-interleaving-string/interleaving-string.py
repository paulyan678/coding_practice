class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        
        def recurse(i, j, k):
            key = (i, j, k)
            if key in memo:
                return memo[key]
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            if i == len(s1) and j == len(s2) and k < len(s3):
                return False
            if k >= len(s3):
                return False

            if i < len(s1) and s1[i] == s3[k] and recurse(i+1, j, k + 1):
                memo[key] = True
                return True
            if j < len(s2) and s2[j] == s3[k] and recurse(i, j + 1, k + 1):
                memo[key] = True
                return True
            memo[key] = False
            return False
        return recurse(0, 0, 0)
            


        
        