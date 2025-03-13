#Thought Process: Was working on a much more complicated version with swapping elements and iterating through each value, but was having trouble passing edge
#cases. Thought that it was too complicated and I must be going about it wrong, so I thought, why not just combine and call sort.

#Results: 0ms, beats 100% time, 93% memory
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()