class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        
        def dfs(r,c):
            # recursion base case
            if not (r in range(rows)) or not (c in range(cols)) or board[r][c] != "O":
                return
            
            board[r][c] = "T"
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        # 1. change all border connected "O"s to another placeholder "T"s (use DFS)
        for i in range(rows):
            for j in range(cols):
                if (i in [0,rows-1]) or (j in [0,cols-1]) and (board[i][j] == "O"):
                    dfs(i,j)
                    
        # 2. iterate entire board, change remaining "O"s into "X"s
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        # 3. change placeholder "T"s back into "O"s
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "T":
                    board[i][j] = "O"