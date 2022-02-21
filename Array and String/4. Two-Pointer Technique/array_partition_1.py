from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        output=int()

        for i in range(0,len(nums),2):
            output+=sorted_nums[i]

        return output

# Driver code
s = Solution()
# Test case 1
print('Executing test case 1: nums = [1,4,3,2]')
print('Output for test case 1: {}'.format(s.arrayPairSum(nums = [1,4,3,2])))

# Test case 2
print('Executing test case 2: nums = [6,2,6,5,1,2]')
print('Output for test case 2: {}'.format(s.arrayPairSum(nums = [6,2,6,5,1,2])))