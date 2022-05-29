class Solution:
    def romanToInt(self, s: str) -> int:
        score = 0
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        for i in range(len(s)-1):
            
            curr = roman_to_int[s[i]]
            nxt = roman_to_int[s[i+1]] 
            
            if curr < nxt:
                score -= curr
            else:
                score += curr
        
        score = score + roman_to_int[s[len(s)-1]]
        
        return score
