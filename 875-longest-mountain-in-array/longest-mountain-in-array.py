import numpy as np
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        dp_up_hill = [0] * len(arr)
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                dp_up_hill[i] = 1 + dp_up_hill[i-1]
        
        dp_down_hill = [0] * len(arr)
        for i in range(len(arr)-2, -1, -1):
            if arr[i] > arr[i+1]:
                dp_down_hill[i] = 1 + dp_down_hill[i+1]
        
        return max([up + down + 1 for up, down in zip(dp_up_hill, dp_down_hill) if up and down], default=0)

        