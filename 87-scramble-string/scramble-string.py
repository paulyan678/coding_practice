class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        @lru_cache(None)
        def recurse(a, b):
            if len(a) == 1:
                return a == b
            
            for i in range(len(a) - 1):
                if (recurse(a[:i+1], b[:i+1]) and recurse(a[i+1:], b[i+1:])) or (recurse(a[:i+1], b[len(b)-i-1:]) and recurse(a[i+1:], b[:len(b)-i-1])):
                    return True
            return False
        return recurse(s1, s2)