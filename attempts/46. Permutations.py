from typing import List
# backtracking solution
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output=list()
        
        # base case to terminate
        if len(nums) == 1:
            return [nums[:]]
        
        # iterate and backtrack
        for i in range(len(nums)):
            n = nums.pop(0)
            permutations = self.permute(nums)
            
            for perm in permutations:
                perm.append(n)
                
            output.extend(permutations)
            nums.append(n)
        
        return output
    
#recursive solution
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.output = []
        self.nums_len = len(nums)

        def recursive(input_list):
            if len(input_list) == self.nums_len:
                self.output.append(input_list)
                return

            for i in range(self.nums_len):
                if nums[i] not in input_list:
                    recursive(input_list + [nums[i]])

        recursive([])
        return self.output

s = Solution()
print(s.permute([1,2,3]))