from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        sorted_nums=sorted(nums)
        if sorted_nums[-1] >= sorted_nums[-2]*2:
            return nums.index(sorted_nums[-1])
        else:
            return -1


# Driver code
s = Solution()
# Test case 1
print('Executing test case 1: nums = [3,6,1,0]')
print('Output for test case 1: {}'.format(s.dominantIndex(nums = [3,6,1,0])))
# Test case 2
print('Executing test case 2: nums = [1,2,3,4]')
print('Output for test case 2: {}'.format(s.dominantIndex(nums = [1,2,3,4])))
# Test case 3
print('Executing test case 3: nums = [1]')
print('Output for test case 3: {}'.format(s.dominantIndex(nums = [1])))
