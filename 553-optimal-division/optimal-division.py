from typing import List

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        # Base case: if there's only one number, return it as a string.
        if len(nums) == 1:
            return str(nums[0])
        # Base case: if there are two numbers, return them in the optimal division format.
        elif len(nums) == 2:
            return f"{nums[0]}/{nums[1]}"
        else:
            # For more than two numbers, the optimal format is first number divided by all the others in parentheses.
            # This is because dividing by the smallest possible result (which is the product of all other numbers)
            # will yield the largest result.
            return f"{nums[0]}/(" + '/'.join(map(str, nums[1:])) + ")"

        