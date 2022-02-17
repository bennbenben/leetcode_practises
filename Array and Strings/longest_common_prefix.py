from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_str_list=sorted(strs)
        common_prefix=""

        for x, y in zip(sorted_str_list[0], sorted_str_list[-1]):
        	if x == y:
        		common_prefix+=x
        	else:
        		break
        return common_prefix

s=Solution()
print(s.longestCommonPrefix(strs = ["flower","flow","flight"]))