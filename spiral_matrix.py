from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral_list=list()
        left, right = 0, len(matrix[0])
        top, btm = 0, len(matrix)

        while left < right and top < btm:

            # iterate across the top row for every element
            for i in range(left, right):
                spiral_list.append(matrix[top][i])
            top+=1

            # iterate down from top right to btm right
            for i in range(top, btm):
                spiral_list.append(matrix[i][right-1])
            right-=1

            if not (left < right and top < btm):
                break

            # iterate across btm right to btm left
            for i in range(right-1, left-1, -1):
                spiral_list.append(matrix[btm-1][i])
            btm-=1

            # iterate from btm left to top left
            for i in range(btm-1, top-1, -1):
                spiral_list.append(matrix[i][left])
            left+=1

        return spiral_list



s = Solution()
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))