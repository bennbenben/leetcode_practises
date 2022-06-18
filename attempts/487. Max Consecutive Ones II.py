class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        num_zeros = 0
        longest_seq = 0
        left = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                num_zeros += 1
            
            while num_zeros >= 2:
                if nums[left] == 0:
                    num_zeros -=1
                left += 1
            
            longest_seq = max(longest_seq, i-left+1)
        
        return longest_seq