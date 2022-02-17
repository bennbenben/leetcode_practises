from typing import List

class Solution:
	def minSubArrayLen(self, target: int, nums: List[int]) -> int:
		l_ptr=total_sum=current_length=0
		best_length=float('inf')

		for i in range(len(nums)):
			total_sum+=nums[i]

			while total_sum >= target:
				current_length = i-l_ptr+1
				best_length = min(best_length, current_length)
				total_sum-=nums[l_ptr]
				l_ptr+=1

		if best_length == float('inf'):
			return 0
		else:
			return best_length 

s = Solution()
print(s.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))