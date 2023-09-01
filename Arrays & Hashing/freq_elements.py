#First Attempt
'''
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}

        for num in nums:
            if num in counts:
                continue
            counts[num] = nums.count(num)

        sortednums = sorted(counts.values())
        results = []
        for i in range(k):
            maxVal = max(counts.values())
            keyInd = counts.values().index(maxVal)
            key = counts.keys()[keyInd]
            results.append(key)
            del counts[key]
        return results
'''
#Results: 1005 ms (5%), 16.49 mb (91.31%)
