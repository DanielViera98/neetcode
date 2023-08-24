nums = [1,2,3,1]

#First Attempt
'''
for i in nums:
    if nums.count(i) > 1:
        return True
return False
'''
#Result: Works, but takes too long.

#Second Attempt
'''
for ind, i in enumerate(nums,0):
    for j in range(ind+1, len(nums)):
        print(nums[j])
        if i == nums[j]:
            return True
return False
'''
#Result: Works but even slower

#Third attempt (using solution as guide)
'''
for i in range (len(nums)-1):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j]:
            return True
return False
'''
#Result: Works, but still too slow

#Solution: (Copy Pasted from solution)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen and seen[num] >= 1:
                return True
            seen[num] = seen.get(num, 0) + 1
        return False