class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_left = [None] * len(nums)
        nums_left[0] = 1
        nums_right = [None] * len(nums)
        nums_right[-1] = 1
        output = list()
        
        for i in range(1, len(nums)):
            nums_left[i] = nums[i-1] * nums_left[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            nums_right[i] = nums[i+1] * nums_right[i+1]
        
        for x, y in zip(nums_left, nums_right):
            output.append(x*y)
        
        return output