from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top_index = left_index = 0
        btm_index, right_index = len(matrix), len(matrix[0])
        output_matrix = list()

        while top_index < btm_index and left_index < right_index:

            # Iterate from right to left
            for i in range(left_index, right_index): # left index = 0, right index = 4
                output_matrix.append(matrix[top_index][i])
            top_index+=1 

            # Iterate from top right to btm right
            for i in range(top_index, btm_index): # top index = 1, btm index = 3
                output_matrix.append(matrix[i][right_index-1])
            right_index-=1 

            if not (top_index < btm_index and left_index < right_index):
                break

            # Iterate from btm right to btm left
            for i in range(right_index-1, left_index-1, -1): # right index = 3, left_index = 0
                output_matrix.append(matrix[btm_index-1][i])
            btm_index-=1

            # Iterate from btm left to top left
            for i in range(btm_index-1,top_index-1,-1):
                output_matrix.append(matrix[i][left_index])
            left_index+=1

        return output_matrix


# Driver code
s = Solution()
# Test case 1
print('Executing test case 1: matrix = [[1,2,3],[4,5,6],[7,8,9]]')
print('Output for test case 1: {}'.format(s.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]])))

# Test case 2
print('Executing test case 2: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]')
print('Output for test case 2: {}'.format(s.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]])))
