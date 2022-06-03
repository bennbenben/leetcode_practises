class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left <= right: # because left can be equal to right
            pivot = (left+right)//2 # left = 0, right = 3, pivot = 1
            
            if nums[pivot] == target:
                return pivot
            
            if nums[pivot] < target: # target is on the right side of pivot element
                left = pivot + 1
            else: # target is on the left side of pivot element
                right = pivot - 1
        
        return left