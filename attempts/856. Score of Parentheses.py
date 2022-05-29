class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        score=0
        for i in s:
            if i =="(":
                stack.append(0)
            
            else:
                last = stack.pop()
                if last == 0:
                    score = 1
                else:
                    score = last *2
                stack[-1] += score
                    
        return stack[-1]