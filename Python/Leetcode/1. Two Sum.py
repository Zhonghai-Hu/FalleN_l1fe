class Solution(object):
    def twoSum(self, nums, target):
        for i,num in enumerate(nums):
            if target - num in nums[i+1:]:
                return [i,nums[i+1:].index(target-num)+i+1]
                