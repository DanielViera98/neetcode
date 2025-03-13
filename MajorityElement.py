#Thought Process: Iterate through the list, assigning each value to a dictionary as a key. If the key exists, iterate the value.
#If the Key doesn't exist, create it with a value of 1. Once a value is greater than n/2, return it. Maximum O(n) Complexity.

#Result: 16ms, beats 9% time, 5% memory.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        stuff = dict({})
        l = len(nums) / 2
        for i in nums:
            if i in stuff:
                stuff[i] = stuff[i] + 1
            else:
                stuff[i] = 1
            if stuff[i] > l:
                return i

#Thought Process: if there is always a majority, then a sorted list will always have the majority value in the middle. Sort list
#and return median number.

#Result: 4ms, beats 70% time, 20% memory.

#Notes: in python, // can be used as a floor operator. Shown in given solution.
class SecondSolution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[floor(len(nums)/2)]
    

#Thought Process: by replacing the floor function with an operator, I can reduce the time by removing the extra computation of
#division + floor.

#Result: 0ms, beats 100% time, 87% memory.
class ThirdSolution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]