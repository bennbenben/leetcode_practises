from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_tri = []
        
        for i in range(numRows):
        	pascal_tri.append([])

        	for j in range(i+1):
        		if j == 0 or j == i:
        			pascal_tri[i].append(1)
        		else:
        			pascal_tri[i].append(
        				pascal_tri[i-1][j]+pascal_tri[i-1][j-1]
        				)

        return pascal_tri

s = Solution()
print(s.generate(numRows=5))