class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        
        while left < right:
            pivot = (left+right)//2
            
            # if left side is sorted, search towards the right
            if nums[pivot] > nums[right]:
                left = pivot + 1
            
            # if right side is sorted, search towards the left
            else:
                right = pivot
        
        return nums[left]