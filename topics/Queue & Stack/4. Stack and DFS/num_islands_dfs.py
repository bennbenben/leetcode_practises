from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        # initialize variables
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        # helper dfs function
        def dfs_islands(i, j):
            if (i in range(rows) and 
                j in range(cols) and
                grid[i][j] == '1'):
                    grid[i][j] = '0'

                    for dr, dc in dirs:
                        r, c = dr+i, dc+j
                        dfs_islands(r,c)

            else:
                return
            

        # iteration
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs_islands(i,j)
                    islands+=1

        return islands


s = Solution()
res = s.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])
print(res)
