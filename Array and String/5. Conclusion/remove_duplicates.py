from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k+=1
        return k



# Driver code
s = Solution()
# Test case 1
print('Executing test case 1: nums = [1,1,2]')
print('Output for test case 1: {}'.format(s.removeDuplicates(nums = [1,1,2])))

# Test case 2
print('Executing test case 2: s = "God Ding"')
print('Output for test case 2: {}'.format(s.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4])))
