#Thought Process: Create an infinite loop, remove the element, and break if the element not found. Used a try-catch statement to break when encountering error.

#Result: 0ms, beats 100% time, 33% memory.
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while True:
            try:
                nums.remove(val)
            except ValueError:
                break
        return len(nums)