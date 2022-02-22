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
            nums[i] = 0

        return nums


# Driver code
s = Solution()
# Test case 1
print('Executing test case 1: nums = [0,1,0,3,12]')
print('Output for test case 1: {}'.format(s.moveZeroes(nums = [0,1,0,3,12])))

# Test case 2
print('Executing test case 2: nums = [0]')
print('Output for test case 2: {}'.format(s.moveZeroes(nums = [0])))

# Test case 2
print('Executing test case 3: nums = [0,0,1]')
print('Output for test case 3: {}'.format(s.moveZeroes(nums = [0,0,1])))
