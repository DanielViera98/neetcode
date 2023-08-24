# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, 
# and j != k, # and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
nums = [-1,0,1,2,-1,-4]
n = len(nums)
for i in range(n):
    x = nums[i]
    for j in range(i,n):
        y = nums[j]
        for k in range(j,n):
            z = nums[k]