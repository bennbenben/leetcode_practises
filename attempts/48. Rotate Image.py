class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix[0])-1
        
        while left < right:
            for i in range(right-left):
                top, btm = left, right
                
                # save the top left variable
                top_left = matrix[top][left+i]
                
                # rotate btm left to top left
                matrix[top][left+i] = matrix[btm-i][left]
                
                # rotate btm right to btm left
                matrix[btm-i][left] = matrix[btm][right-i]
                
                # rotate top right to btm right
                matrix[btm][right-i] = matrix[top+i][right]
                
                # rotate top left to top right
                matrix[top+i][right] = top_left
            
            left += 1
            right -= 1