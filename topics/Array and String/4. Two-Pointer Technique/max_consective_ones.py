from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive_count=int()
        k=0

        for i in range(len(nums)):
            if nums[i] == 1:
                consecutive_count+=1
                if consecutive_count>k:
                    k=consecutive_count
            else:
                consecutive_count=0
        return k

# Driver code
s = Solution()
# Test case 1
print('Executing test case 1: nums = [1,1,0,1,1,1]')
print('Output for test case 1: {}'.format(s.findMaxConsecutiveOnes(nums = [1,1,0,1,1,1])))

# Test case 2
print('Executing test case 2: nums = [1,0,1,1,0,1]')
print('Output for test case 2: {}'.format(s.findMaxConsecutiveOnes(nums = [1,0,1,1,0,1])))