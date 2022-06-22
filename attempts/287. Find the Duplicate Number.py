# Using set()
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        output = set()
        for n in nums:
            if n in output:
                return n
            else:
                output.add(n)

# Use collections.Counter                
from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_count = Counter(nums)
        for key, val in nums_count.items():
            if val > 1:
                return key

# Sorting Solution
class Solution:                
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]