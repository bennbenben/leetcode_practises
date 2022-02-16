from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums_sorted=sorted(nums)
        print(nums_sorted)
        accumulated_sum=0

        for i in range(0,len(nums),2):
            accumulated_sum+=nums_sorted[i]
            # print('iteration number: {},accumulated_sum:{}'.format(i,accumulated_sum))
        return accumulated_sum


s = Solution()
print(s.arrayPairSum(nums = [1,4,3,2]))