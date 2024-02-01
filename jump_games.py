def jump_games(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) == 1:
        return True
    if nums[0] == 0:
        return False
    if nums[0] >= len(nums) - 1:
        return True
    for i in range(1, nums[0] + 1):
        if jump_games(nums[i:]):
            return True
    return False