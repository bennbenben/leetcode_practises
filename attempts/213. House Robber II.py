class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return max(nums)
        
        nums_1 = nums[:-1]
        nums_image_1 = [1]*len(nums_1)
        nums_image_1[0]=nums_1[0]
        nums_image_1[1]=max(nums_1[0],nums_1[1])
        for i in range(2,len(nums_1)):
            nums_image_1[i] = max(nums_1[i]+nums_image_1[i-2],nums_image_1[i-1])
        
        
        nums_2 = nums[1:]
        nums_image_2 = [1]*len(nums_2)
        nums_image_2[0]=nums_2[0]
        nums_image_2[1]=max(nums_2[0],nums_2[1])
        for i in range(2,len(nums_1)):
            nums_image_2[i] = max(nums_2[i]+nums_image_2[i-2],nums_image_2[i-1])
        
        return max(nums_image_1[-1],nums_image_2[-1])