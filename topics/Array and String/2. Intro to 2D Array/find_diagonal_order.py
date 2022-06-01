from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        num_rows = len(mat)
        num_cols = len(mat[0])

        # Create output shell to assign elements for diagonal traversal
        num_diagonals = num_rows+num_cols-1 # no. of diagonals is observed to be (m+n)-1
        diagonals=list()
        [diagonals.append([]) for i in range(num_diagonals)]

        # Execute diagonal traversal - element mat[i][j] is appended to diagonals[i+j]
        for i in range(num_rows):
            for j in range(num_cols):
                diagonals[i+j].append(mat[i][j])
        # print(diagonals)

        # Invert diagonals[even_index]
        for x, y in enumerate(diagonals):
            if x%2==0:
                diagonals[x]=y[::-1]
        # print(diagonals)

        # Output in specific format
        diagonals_invert=list()
        for i in diagonals:
            for j in i:
                diagonals_invert.append(j)

        return diagonals_invert

# Driver code
s = Solution()
# Test case 1
print('Executing test case 1: mat = [[1,2,3],[4,5,6],[7,8,9]]')
print('Output for test case 1: {}'.format(s.findDiagonalOrder(mat = [[1,2,3],[4,5,6],[7,8,9]])))
# Test case 2
print('Executing test case 2: mat = [[1,2],[3,4]]')
print('Output for test case 2: {}'.format(s.findDiagonalOrder(mat = [[1,2],[3,4]])))
