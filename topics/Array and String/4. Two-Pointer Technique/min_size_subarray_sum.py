from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        k, curr_len, curr_sum = 0,0,0
        best_len=float('inf')
        # sorted_nums = sorted(nums)
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            
            while curr_sum >= target:
                curr_len = i-k+1
                best_len = min(best_len, curr_len)
                curr_sum -= nums[k]
                k+=1
        
        return 0 if best_len == float('inf') else best_len

# Driver code
s = Solution()
# Test case 1
print('Executing test case 1: target = 7, nums = [2,3,1,2,4,3]')
print('Output for test case 1: {}'.format(s.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])))

# Test case 2
print('Executing test case 2: target = 4, nums = [1,4,4]')
print('Output for test case 2: {}'.format(s.minSubArrayLen(target = 4, nums = [1,4,4])))

# Test case 3
print('Executing test case 3: target = 11, nums = [1,1,1,1,1,1,1,1]')
print('Output for test case 3: {}'.format(s.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1])))
