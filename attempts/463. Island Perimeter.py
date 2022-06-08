class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r,c):
            # recursive base case
            if not (r in range(rows) and c in range(cols)) \
            or grid[r][c]==0:
                return 1
            if (r,c) in visited:
                return 0
            
            visited.add((r,c))
            
            right = dfs(r,c+1)
            left = dfs(r, c-1)
            top = dfs(r+1, c)
            btm = dfs(r-1, c)
            
            return right+left+top+btm
        
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    return dfs(i,j)