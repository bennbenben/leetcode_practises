# my solution
class Solution:
    def swap(self, nums, left, right):
        nums[left], nums[right] = nums[right], nums[left]
        return nums
        
    def reverse(self, nums, start_idx, end_idx):
        while start_idx < end_idx:
            nums[start_idx], nums[end_idx] = nums[end_idx], nums[start_idx]
            start_idx += 1
            end_idx -= 1
        return nums
        
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dec_pointer = -1
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i-1] < nums[i]:
                dec_pointer = i-1
                break
        
        inc_pointer = dec_pointer+1
        # print("dec pointer is: ", dec_pointer, "value is: ", nums[dec_pointer])
        # print("inc pointer is: ", inc_pointer, "value is: ", nums[inc_pointer])        
        nums = self.reverse(nums, inc_pointer, len(nums)-1)
        # print(nums)
        
        if dec_pointer == -1:
            return 
        
        for i in range(dec_pointer, len(nums)):
            if nums[i] > nums[dec_pointer]:
                nums = self.swap(nums, dec_pointer, i)
                return 

# youtube solution
class Solution:
    def swapNums(self, nums, start_index, end_index):
        temp_var = nums[start_index]
        nums[start_index] = nums[end_index]
        nums[end_index] = temp_var
        return nums
        
    def reverseNums(self, nums, start_index, end_index):
        while start_index < end_index:
            self.swapNums(nums, start_index, end_index)
            start_index += 1
            end_index -= 1
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1. iterate backwards until u stop ascending
        2. reverse all the ascending elements
        3. iterate forward from the one u stopped at originally, to swap with a number just greater than that
        """
        if len(nums) == 1:
            return
        if len(nums) == 2:
            return self.swapNums(nums, 0, 1)
        
        decrement_pointer = len(nums)-2
        while decrement_pointer >= 0 and nums[decrement_pointer] >= nums[decrement_pointer+1]:
            decrement_pointer -= 1
        self.reverseNums(nums, decrement_pointer+1, len(nums)-1)
        
        if decrement_pointer == -1:
            return
        
        increment_pointer = decrement_pointer + 1
        while nums[increment_pointer] <= nums[decrement_pointer] and increment_pointer < len(nums):
            increment_pointer+=1
        
        self.swapNums(nums, decrement_pointer, increment_pointer)
        return