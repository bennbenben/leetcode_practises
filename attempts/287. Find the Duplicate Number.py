# Using set()
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        output = set()
        for n in nums:
            if n in output:
                return n
            else:
                output.add(n)

# Sorting Solution
class Solution:                
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]