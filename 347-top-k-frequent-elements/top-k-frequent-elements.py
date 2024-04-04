class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        count_list = list(count.items())
        count_list = sorted(count_list, key=lambda x:x[1], reverse=True)
        return [count_list[i][0] for i in range(k)]
        