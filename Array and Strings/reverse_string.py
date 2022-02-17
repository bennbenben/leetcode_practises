from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l_ptr=0
        r_ptr=len(s)-1
        # s_output=""

        while l_ptr<r_ptr:
            s[l_ptr], s[r_ptr] = s[r_ptr], s[l_ptr]
            l_ptr+=1
            r_ptr-=1
            # print(s)

s = Solution()
s.reverseString(s = ["h","e","l","l","o"])