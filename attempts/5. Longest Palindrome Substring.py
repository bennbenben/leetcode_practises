class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome, max_palindrome = str(), str()
        len_palindrome, max_palin_len = int(), int()
        
        for i in range(len(s)):
            # case when len(string) is odd
            left, right = i, i
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindrome = s[left:right+1]
                len_palindrome = right-left+1
                
                if len_palindrome > max_palin_len:
                    max_palindrome = palindrome
                    max_palin_len = len_palindrome
                    
                left -= 1
                right += 1
            
            # case when len(string) is even
            left, right = i, i+1
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindrome = s[left:right+1]
                len_palindrome = right-left+1
                
                if len_palindrome > max_palin_len:
                    max_palindrome = palindrome
                    max_palin_len = len_palindrome
                    
                left -= 1
                right += 1
        
        return max_palindrome

inp = "cbbd"
print(inp[::-1])
