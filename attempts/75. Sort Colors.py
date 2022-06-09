# Bubble Sort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]>nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
        
        print(nums)

# Merge Sort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def merge_sort(nums):
            if len(nums)>1:
                # splitting
                left_arr = nums[:len(nums)//2]
                right_arr = nums[len(nums)//2:]

                # recursion
                merge_sort(left_arr)
                merge_sort(right_arr)
                
                # merge
                i, j, k = 0, 0, 0 #left, right, and merged array indexes
                
                while i < len(left_arr) and j < len(right_arr):
                    if left_arr[i] < right_arr[j]:
                        nums[k] = left_arr[i]
                        i += 1
                        k += 1
                    else:
                        nums[k] = right_arr[j]
                        j += 1
                        k += 1
                
                # transfer remaining elements in left arr into merged arr
                while i < len(left_arr):
                    nums[k] = left_arr[i]
                    i += 1
                    k += 1
                
                # transfer remaining elements in right arr into merged arr
                while j < len(right_arr):
                    nums[k] = right_arr[j]
                    j += 1
                    k += 1