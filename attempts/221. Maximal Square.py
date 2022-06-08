class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        cache = {}
        
        def helper(r,c):
            # recursion base case
            if not (r in range(rows) and c in range(cols)):
                return 0
            
            # start recursion
            if (r,c) not in cache.keys():
                cache[(r,c)] = 0
                right = helper(r, c+1)
                diag = helper(r+1, c+1)
                btm = helper(r+1, c)
                
                if matrix[r][c] == "1":
                    cache[(r,c)] = 1 + min(right,diag,btm)
            
            return cache[(r,c)]
        
        helper(0,0)
        return max(cache.values())**2