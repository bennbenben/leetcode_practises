from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums_sum=sum(nums)

        for i in range(len(nums)):
            left_sum=sum(nums[:i])
            right_sum=nums_sum-left_sum-nums[i]
            # print('iteration:{},left_sum:{},right_sum:{}'.format(i,left_sum,right_sum))
            if left_sum==right_sum:
                return i
        return -1

# Driver code
s = Solution()
# Test case 1
print('Executing test case 1: nums = [1,7,3,6,5,6]')
print('Output for test case 1: {}'.format(s.pivotIndex(nums = [1,7,3,6,5,6])))
# Test case 2
print('Executing test case 2: nums = [1,2,3]')
print('Output for test case 2: {}'.format(s.pivotIndex(nums = [1,2,3])))
# Test case 3
print('Executing test case 3: nums = [2,1,-1]')
print('Output for test case 3: {}'.format(s.pivotIndex(nums = [2,1,-1])))
