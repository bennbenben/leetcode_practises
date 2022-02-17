from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k+=1
        
        for i in range(k,len(nums)):
            nums[i]=0

        return nums

s = Solution()
print(s.moveZeroes(nums = [0,1,0,3,12]))            