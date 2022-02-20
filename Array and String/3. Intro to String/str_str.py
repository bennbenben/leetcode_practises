class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

# Driver code
s = Solution()
# Test case 1
print('Executing test case 1: haystack = "hello", needle = "ll"')
print('Output for test case 1: {}'.format(s.strStr(haystack = "hello", needle = "ll")))

# Test case 2
print('Executing test case 2: haystack = "aaaaa", needle = "bba"')
print('Output for test case 2: {}'.format(s.strStr(haystack = "aaaaa", needle = "bba")))

# Test case 3
print('Executing test case 3: haystack = "", needle = ""')
print('Output for test case 3: {}'.format(s.strStr(haystack = "", needle = ""))) 