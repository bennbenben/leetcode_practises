# BFS solution
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),  len(grid[0])
        visited, max_area = set(), 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def bfs(i,j):
            area = 1
            q = deque()
            q.append((i,j))
            visited.add((i,j))
            
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r = dr+row
                    c = dc+col
                    if r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c]==1:
                        area += 1
                        q.append((r,c))
                        visited.add((r,c))
            return area
        
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j]==1:
                    island_area = bfs(i,j)
                    max_area = max(max_area, island_area)
        return max_area

# DFS solution
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        island_area, max_area = 0, 0
        visited = set()
        
        def dfs(i,j):
            # recursive base case
            if not (i in range(rows) and j in range(cols) and (i,j) not in visited and grid[i][j]==1):
                return 0
            
            visited.add((i,j))
            
            # recursive call
            return (1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1))
        
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j] == 1:
                    island_area = dfs(i,j)
                    max_area = max(island_area, max_area)
        
        return max_area