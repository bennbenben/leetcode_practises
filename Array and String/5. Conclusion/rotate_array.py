from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            # extract=nums.pop()
            nums.insert(0,nums.pop())
        return nums

# Driver code
s = Solution()
# Test case 1
print('Executing test case 1: nums = [1,2,3,4,5,6,7], k = 3')
print('Output for test case 1: {}'.format(s.rotate(nums = [1,2,3,4,5,6,7], k = 3)))

# Test case 2
print('Executing test case 2: nums = [-1,-100,3,99], k = 2')
print('Output for test case 2: {}'.format(s.rotate(nums = [-1,-100,3,99], k = 2)))
