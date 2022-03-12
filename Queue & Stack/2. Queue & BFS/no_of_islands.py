class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        # initialize variables
        rows, cols = len(grid), len(grid[0])
        visited=set()
        num_islands=0
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]

        # helper function: bfs_islands
        def bfs_islands(i,j):
            q = deque()
            q.append((i,j))
            visited.add((i,j))

            while q:
                row, col = q.popleft()

                for dr, dc in dirs:
                    r, c = row + dr, col + dc

                    if (r in range(rows) and
                        c in range(cols) and
                        (r,c) not in visited and
                        grid[r][c] == "1"):

                        q.append((r,c))
                        visited.add((r,c))

        # traverse the grid
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j] == "1":
                    bfs_islands(i,j)
                    num_islands+=1
        return num_islands
