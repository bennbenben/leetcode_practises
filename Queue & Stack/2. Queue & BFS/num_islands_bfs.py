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

        # helper bfs function
        def bfs_islands(i, j):
            q = deque()
            q.append((i,j))
            visited.add((i,j))

            while q:
                r, c = q.popleft()

                for dir_idx in range(len(dirs)):
                    dr, dc = dirs[dir_idx][0] + r, dirs[dir_idx][1] + c

                    if (grid[dr][dc] == '1' and
                        (dr, dc) not in visited and
                        0 <= dr < rows and 
                        0 <= dc < cols):
                        q.append((dr,dc))
                        visited.add((dr,dc))

        # iteration
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j] == '1':
                    bfs_islands(i,j)
                    islands += 1

        return islands


s = Solution()
res = s.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])
print(res)
