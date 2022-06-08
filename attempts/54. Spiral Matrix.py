class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, left = 0, 0
        bottom, right = len(matrix), len(matrix[0]) 
        output = list()
        
        #top,left=0,0
        #bottom,right=3,3
        
        while top < bottom and left < right:
            # output from left to right
            for i in range(left,right): # 0 to 3
                output.append(matrix[top][i])
            top += 1 # top = 1
            
            # output from top right to btm right
            for i in range(top, bottom): #(1, 3)
                output.append(matrix[i][right-1])
            right -= 1 # right = 2
            
            if not (top < bottom and left < right):
                return output
            
            # output from btm right to btm left
            for i in range(right-1, left-1, -1): # (1, -1)
                output.append(matrix[bottom-1][i])
            bottom -= 1 # bottom = 2
            
            # output from btm left to middle left
            for i in range(bottom-1, top-1, -1): # (1,0)
                output.append(matrix[i][left])
            left += 1
        
        return output