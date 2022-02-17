from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        num_row, num_col = len(mat), len(mat[0])
        num_diagonals = num_row+num_col-1 # number of diagonals is observed to be this formula

        diagonals = [[] for _ in range(num_diagonals)]

        # each element[i][j] is observed to be appended to the diagonal (i+j)
        for i in range(num_row):
             for j in range(num_col):
                diagonals[i+j].append(mat[i][j])

        # if index is odd, then flip reverse the digits
        res = diagonals[0]
        # res=list([])
        for i in range(1, len(diagonals)):
            # print(diagonals[i])
            if i%2 == 0:
                res.extend([*reversed(diagonals[i])])
            else:
                # print(diagonals[i])
                res.extend(diagonals[i])

        return res 


sol_init = Solution()
print(sol_init.findDiagonalOrder(mat = [[1,2,3],[4,5,6],[7,8,9]]))