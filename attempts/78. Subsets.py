class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = list()
        curr = list()
        i=0
        
        def dfs(i, curr):
            # base case of recursion
            if i == len(nums):
                output.append(curr.copy())
                return 
            
            # case to include nums[i]
            curr.append(nums[i])
            dfs(i+1,curr)
            
            # case not to include nums[i]
            curr.pop()
            dfs(i+1, curr)
        
        dfs(i, curr)
        return output