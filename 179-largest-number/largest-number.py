class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Sort numbers based on the best concatenation order
        largest_num = ''.join(sorted(map(str, nums), key=lambda x: x*10, reverse=True))
        # Return '0' if the first character is '0', otherwise return the concatenated string
        return '0' if largest_num[0] == '0' else largest_num