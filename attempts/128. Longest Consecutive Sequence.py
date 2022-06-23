class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # sort the array
        nums.sort()
        print(nums)
        max_len = consecutive = 1
        
        # iterate from idx1 onwards
        for i in range(1, len(nums)):
            # interested in non-duplicates
            if nums[i] != nums[i-1]:
                # check if increment is += 1
                if nums[i] - nums[i-1] == 1:
                    consecutive += 1
                # start a new set of counters
                else:
                    max_len = max(max_len, consecutive)
                    consecutive = 1
        
        # if ended on consecutive += 1 loop
        max_len = max(max_len, consecutive)
        
        return max_len