class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # get variables
        rows, cols = len(rooms), len(rooms[0])
        q = deque()
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # append the cells where they represent a gate to the q
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))

        def validate_moves(i, j):
            if (i<0 or i == rows or j<0 or j == cols or 
                (i,j) in visited or rooms[i][j] == -1):
                return
            else:
                q.append((i,j))
                visited.add((i,j))

        dist=0
        # start the BFS traversal
        while q:

            # iterate across all nodes in the given layer
            for _ in range(len(q)):
                i, j = q.popleft()
                rooms[i][j] = dist

                for index in range(len(directions)):
                    validate_moves(i+directions[index][0], j+directions[index][1])

            dist+=1
