class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_str = str()
        for i in s:
            if i.isalnum():
                filtered_str += i.lower()
        
        i, j = 0, len(filtered_str)-1
        while i<j:
            if filtered_str[i] != filtered_str[j]:
                return False
            i += 1
            j -= 1
        return True       

class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_str = str()
        for i in s:
            if i.isalnum():
                filtered_str += i.lower()

        if filtered_str == filtered_str[::-1]:
            return True
        else:
            return False

s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))