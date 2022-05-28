from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        
        nums_image = [1]*len(nums)
        nums_image[0]=nums[0]
        nums_image[1]=max(nums[0],nums[1])
        
        for i in range(2, len(nums)):
            nums_image[i] = max(nums[i] + nums_image[i-2], nums_image[i-1])
        return nums_image[-1]
