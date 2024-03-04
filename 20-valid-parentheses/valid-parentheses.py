class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_open_pair = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c not in close_open_pair:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                pre_open = stack.pop()
                if pre_open != close_open_pair[c]:
                    return False
        if len(stack) != 0:
            return False
        return True
            
            
        