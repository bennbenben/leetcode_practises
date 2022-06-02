class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        prefix_path = path.split("/")
        
        for i in range(len(prefix_path)):
            if prefix_path[i] == "..":
                if stack:
                    stack.pop()
            
            elif prefix_path[i] == "." or prefix_path[i] == "":
                continue
            
            else:
                stack.append(prefix_path[i])
        
        return "/" + "/".join(stack)