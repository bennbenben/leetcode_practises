from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1

        return k

# Driver code
s = Solution()
# Test case 1
print('Executing test case 1: nums = [3,2,2,3], val = 3')
print('Output for test case 1: {}'.format(s.removeElement(nums = [3,2,2,3], val = 3)))

# Test case 2
print('Executing test case 2: nums = [0,1,2,2,3,0,4,2], val = 2')
print('Output for test case 2: {}'.format(s.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)))