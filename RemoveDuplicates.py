#Thoughts: first idea, iterate through list, add items to list as they are found. if the number already exists in list, pop from nums. return length.

#Results: 90ms, beats 5% time, 9% space
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numbers = []
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] in numbers:
                nums.pop(i)
            else:
                numbers.append(nums[i])
                i += 1
            length = len(nums)
        return length

#Thought: Immediate improvement on the same idea, use dictionary instead of list.

#Results: 59ms, beats 8% time, 49%-75% space
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numbers = {}
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] in numbers:
                nums.pop(i)
            else:
                numbers[nums[i]] = 1
                i += 1
            length = len(nums)
        return length

#Thought: Originally, just iterate through, setting the value in dict to 1. End up with a dict length k and by calling keys() can get a list of the unique numbers.
#However, replacing nums with that list was not working, since it is not modifying the original memory. 
#So I expanded it to just copy manually the keys list to nums, and pop the remaining values.

#result: 6ms, beats 18% time, 50% space
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numbers = {}
        for i in range(len(nums)):
                numbers[nums[i]] = 1
        for j in range(len(nums)):
            if j < len(numbers):
                nums[j] = list(numbers.keys())[j]
            else:
                nums.pop()
        return len(numbers)
    
#Thought: modify the original list by using the slice function to remove everything, and set equal to the new list.

#result: 3ms, beats 48% time, 30% space
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numbers = {}
        for i in range(len(nums)):
                numbers[nums[i]] = 1
        nums[:] = list(numbers.keys())
        return len(numbers)

#Taken from solution (didn't want to spend more time on it)
#Thoughts: I neglected the fact that the list must already be sorted when given. My solution works for a randomized or sorted list, and so functions as a
#good general program. But since it's sorted, all that needs to be done is navigate the list with two pointers, setting the beginning elements to the unique
#values. Since the rest of the list past j doesn't matter, this works.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j