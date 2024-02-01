def longest_increasing(nums):
    if len(nums) == 1:
        return 1
    mid = len(nums) // 2
    left = longest_increasing(nums[:mid])
    right = longest_increasing(nums[mid:])
    if nums[mid - 1] < nums[mid]:
        return max(left, right + 1)
    else:
        return max(left, right)

print(longest_increasing([1,2,3,4,5,6,7,8,9,10]))