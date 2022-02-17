from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Create the skeleton of pascal triangle
        pascal_tri=[]
        for i in range(rowIndex+1):
            pascal_tri.append([])

            for j in range(i+1):
                if j==0 or j==i:
                    pascal_tri[i].append(1)
                else:
                    pascal_tri[i].append(pascal_tri[i-1][j-1]+pascal_tri[i-1][j])

        # Select and return the row index
        return pascal_tri[rowIndex]

s = Solution()
print(s.getRow(rowIndex = 3))