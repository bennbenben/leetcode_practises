from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l_ptr=0
        r_ptr=len(s)-1

        while l_ptr < r_ptr:
            # Execute swap
            s[l_ptr], s[r_ptr] = s[r_ptr], s[l_ptr]

            # Increment left and right pointer
            l_ptr+=1
            r_ptr-=1

        return s

# Driver code
s = Solution()
# Test case 1
print('Executing test case 1: s = ["h","e","l","l","o"]')
print('Output for test case 1: {}'.format(s.reverseString(s = ["h","e","l","l","o"])))

# Test case 2
print('Executing test case 2: s = ["H","a","n","n","a","h"]')
print('Output for test case 2: {}'.format(s.reverseString(s = ["H","a","n","n","a","h"])))
