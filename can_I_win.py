def canIWin(maxChoosableInteger, desiredTotal):
    memo = {}
    if sum([i for i in range(maxChoosableInteger+1)]) < desiredTotal:
        return False
    def recurse(used, sub_goal):
        key = (used, sub_goal)
        if all(used):
            memo[key] = False
            return False
        
        if key in memo:
            return memo[key]
        for use_num in range(1, maxChoosableInteger + 1):
            if used[use_num]:
                continue
            
            if use_num >= sub_goal:
                memo[key] = True
                return True
            
            if not recurse(used[:use_num] + (True,) + used[use_num+1:], sub_goal - use_num):
                memo[key] = True
                return True
        memo[key] = False
        return False
    
    used = (False,) * (maxChoosableInteger + 1)
    return recurse(used, desiredTotal)

print(canIWin(5, 50))
             




    