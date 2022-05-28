from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis[i] = max(lis[i],lis[j]+1)
        return max(lis)

class Solution:
	def lengthOfLis(self, nums: List[int]) -> int:
		lis = [1] * len(nums)

		for i in range(len(nums)-1, -1, -1):
			for j in range(i+1,len(nums)):
				if nums[i] < nums[j]:
					lis[i] = max(lis[i],lis[j]+1)

		return max(lis)

s= Solution()
print(s.lengthOfLis([10,9,2,5,3,7,101,18]))
