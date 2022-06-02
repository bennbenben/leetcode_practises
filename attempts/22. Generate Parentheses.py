class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 1. only can add open bracket if #open_bracket <= n
        # 2. only can add close bracket if #close_bracket < #open_bracket
        # 3. base condition - #open_bracket = #close_bracket
        curr, output = list(), list()
        open_bracket, close_bracket = int(0), int(0)
        
        def dfs(open_bracket, close_bracket, curr):
            # base condition:
            if open_bracket == close_bracket == n:
                output.append("".join(curr))
                return
            
            # recursive condition - add open bracket
            if open_bracket <= n:
                curr.append("(")
                dfs(open_bracket+1, close_bracket, curr)
                curr.pop()
            
            # recursive condition - add close bracket
            if close_bracket < open_bracket:
                curr.append(")")
                dfs(open_bracket, close_bracket+1, curr)
                curr.pop()
        
        dfs(open_bracket, close_bracket, curr)
        return output