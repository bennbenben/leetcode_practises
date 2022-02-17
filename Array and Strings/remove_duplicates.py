from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1

        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]: # also works: nums[i] != nums[i-1]
                nums[k] = nums[i]
                k+=1
        print(nums)
        return k


s = Solution()
print(s.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))