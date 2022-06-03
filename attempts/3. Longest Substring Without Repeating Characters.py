class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, max_len = 0, 0
        chars = set()
        
        for i in range(len(s)):
            while s[i] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[i])
            max_len = max(max_len, len(chars))
        
        return max_len