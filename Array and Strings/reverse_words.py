from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:
        s_strip = s.strip()
        s_format = s_strip.split(" ")
        s_output = []

        for i in s_format:
            if i == "":
                continue
            else:
                s_output.append(i)
        s_output = " ".join(s_output[::-1])
        return s_output

s = Solution()
print(s.reverseWords(s = "  hello     world  "))