from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        # Initialize variables to create the pyramid
        pascal_triangles = list()
        for i in range(numRows):
            pascal_triangles.append([])

        # Build the pyramid
        for i in range(numRows):
            for j in range(i+1):
                if j==0 or j==(i):
                    pascal_triangles[i].append(1)
                else:
                    pascal_triangles[i].append(pascal_triangles[i-1][j-1]+pascal_triangles[i-1][j])

        return pascal_triangles


# Driver code
s = Solution()
# Test case 1
print('Executing test case 1: numRows = 5')
print('Output for test case 1: {}'.format(s.generate(numRows = 5)))

# Test case 2
print('Executing test case 2: numRows = 1')
print('Output for test case 2: {}'.format(s.generate(numRows = 1)))