from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Create skeleton of pascal's triangle
        pascal_tri = list()
        for i in range(rowIndex+1):
            pascal_tri.append([])

        # Assign values into pascal's triangle
        for i in range(rowIndex+1):
            for j in range(i+1):
                if j==0 or j==i:
                    pascal_tri[i].append(1)
                else:
                    pascal_tri[i].append(pascal_tri[i-1][j-1]+pascal_tri[i-1][j])

        return pascal_tri[rowIndex]

# Driver code
s = Solution()
# Test case 1
print('Executing test case 1: rowIndex = 3')
print('Output for test case 1: {}'.format(s.getRow(rowIndex = 3)))

# Test case 2
print('Executing test case 2: rowIndex = 0')
print('Output for test case 2: {}'.format(s.getRow(rowIndex = 0)))

# Test case 3
print('Executing test case 3: rowIndex = 1')
print('Output for test case 3: {}'.format(s.getRow(rowIndex = 1)))
