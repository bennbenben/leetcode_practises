class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        mod = (10**9)+7
        output = 0
        
        while left <= right:
            curr_sum = nums[left] + nums[right]
            if curr_sum <= target:
                output += pow(2, right-left,mod)
                # output += (2**(right-left))%mod this will time limit exceeded
                left += 1
            else:
                right -= 1
        
        return output%mod