class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        memo = {}
        def can_frog_reach_i_with_k(position, last_jump):
            if position == stones[-1]:
                return True
            key = (position, last_jump)
            if key in memo:
                return memo[key]
            for next_jump in range(last_jump-1, last_jump+2):
                land_pos = position + next_jump
                if (next_jump > 0) and (land_pos in stones) and can_frog_reach_i_with_k(land_pos, next_jump):
                    memo[key] = True
                    return True
            memo[key] = False
            return False
        return can_frog_reach_i_with_k(1, 1)
