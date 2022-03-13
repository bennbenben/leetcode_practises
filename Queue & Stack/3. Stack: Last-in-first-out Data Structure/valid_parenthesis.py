class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        bracket_mapping={
            ")":"(",
            "]":"[",
            "}":"{"
        }
        
        for char in s:
            
            # if char is an open bracket
            if char not in bracket_mapping:
                stack.append(char)
            
            # if char is a closing bracket
            else:
                if stack != []:
                    top_element = stack.pop()
                else:
                    return False
            
                if top_element != bracket_mapping[char]:
                    return False
        
        if not stack:
            return True
        else:
            return False