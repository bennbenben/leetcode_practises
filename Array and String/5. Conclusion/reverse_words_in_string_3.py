from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:
        s_output=list()

        for i in s.split():
            s_output.append(i[::-1])
            
        return " ".join(s_output)



# Driver code
s = Solution()
# Test case 1
print('Executing test case 1: s = "Let\'s take LeetCode contest"')
print('Output for test case 1: {}'.format(s.reverseWords(s = "Let's take LeetCode contest")))

# Test case 2
print('Executing test case 2: s = "God Ding"')
print('Output for test case 2: {}'.format(s.reverseWords(s = "God Ding")))
