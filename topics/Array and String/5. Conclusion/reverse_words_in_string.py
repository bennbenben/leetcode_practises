from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip(" ").split()[::-1])


# Driver code
s = Solution()
# Test case 1
print('Executing test case 1: s = "the sky is blue"')
print('Output for test case 1: {}'.format(s.reverseWords(s = "the sky is blue")))

# Test case 2
print('Executing test case 2: s = "  hello world  "')
print('Output for test case 2: {}'.format(s.reverseWords(s = "  hello world  ")))

# Test case 3
print('Executing test case 3: s = "a good   example"')
print('Output for test case 3: {}'.format(s.reverseWords(s = "a good   example")))
