# Use Python collections.Counter
from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums_count = Counter(nums)
        output = list()
        
        for key, val in nums_count.items():
            if val >= 2:
                output.append(key)
        
        return output

# Use Sorting
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        print(nums)
        left = 0
        output = list()
        
        for i in range(1, len(nums)):
            if nums[i] != nums[left]:
                left += 1
            else:
                output.append(nums[left])
                left += 1
                
        return output