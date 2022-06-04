class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            pivot = (left+right)//2

            # find array middle element value
            if nums[pivot] == target:
                return pivot

            # meaning left side of the array is sorted
            if nums[pivot] > nums[right]:

                # if target is in the left side of pivot
                # (second condition is needed because array is rotated)
                if target < nums[pivot] and nums[left] <= target:
                    right = pivot - 1

                # target is in the right side of pivot
                else:
                    left = pivot + 1
            
            # right side of array is sorted
            else:
                # if target is in the right side of pivot
                # (second condition is needed because array is rotated)
                if nums[pivot] < target and target <= nums[right]:
                    left = pivot + 1
                
                # if target is in the left side of pivot
                else:
                    right = pivot - 1
                    
        return -1