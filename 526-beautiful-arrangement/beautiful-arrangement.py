class Solution:
    def countArrangement(self, n: int) -> int:
        available = [1] * n
        ans = 0

        def backtrack(cur_index):
            nonlocal ans  # To modify ans inside this nested function
            if cur_index > n:
                ans += 1
                return
            for i in range(1, n + 1):  # Iterate through numbers 1 to n
                if available[i - 1] and (cur_index % i == 0 or i % cur_index == 0):
                    available[i - 1] = 0  # Mark as used
                    backtrack(cur_index + 1)
                    available[i - 1] = 1  # Reset for the next iteration
        backtrack(1)  # Start with index 1 since we're dealing with positions, not zero-based index
        return ans
