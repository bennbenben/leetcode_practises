class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_len, left = 0, 0
        
        for i in range(len(s)):
            if s[i] in count.keys():
                count[s[i]] += 1
            else:
                count[s[i]] = 1
            
            if (i-left+1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, i-left+1)
        return max_len