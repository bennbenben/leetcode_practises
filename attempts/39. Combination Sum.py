class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        curr, output = list(), list()
        i, total = int(0), int(0)
        
        def dfs(i, curr, total):
            # base case to accept
            if total == target:
                output.append(curr.copy())
                return
            
            # base case to reject and stop recursion
            if i >= len(candidates) or total > target:
                return
        
            # append and recur
            curr.append(candidates[i])
            dfs(i, curr, total+candidates[i])
            curr.pop()
            dfs(i+1, curr, total)
        
        dfs(i, curr, total)
        return output