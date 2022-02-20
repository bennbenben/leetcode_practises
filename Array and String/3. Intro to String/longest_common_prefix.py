from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_strs = sorted(strs)
        output=str()

        for x,y in zip(sorted_strs[0],sorted_strs[-1]):
            # print('x,y:{},{}'.format(x,y))
            if x==y:
                output+=x
            else:
                break

        return output


# Driver code
s = Solution()
# Test case 1
print('Executing test case 1: strs = ["flower","flow","flight"]')
print('Output for test case 1: {}'.format(s.longestCommonPrefix(strs = ["flower","flow","flight"])))

# Test case 2
print('Executing test case 2: strs = ["dog","racecar","car"]')
print('Output for test case 2: {}'.format(s.longestCommonPrefix(strs = ["dog","racecar","car"])))
