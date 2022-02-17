from typing import List

class Solution:
	def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
		max_consecutive_score=0
		k=0

		for i in range(len(nums)):
			if nums[i] == 1:
				k+=1
				if k>max_consecutive_score:
					max_consecutive_score=k
			else:
				k=0
		return max_consecutive_score



s = Solution()
print(s.findMaxConsecutiveOnes(nums = [1,0,1,1,0,1]))