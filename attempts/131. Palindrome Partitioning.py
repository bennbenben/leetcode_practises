class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = list()
        
        def dfs(curr, word):
            if not word:
                output.append(curr.copy())
                return
            
            for i in range(1, len(word)+1):
                arr = word[:i]
                
                if arr == arr[::-1]:
                    curr.append(arr)
                    dfs(curr, word[i:])
                    curr.pop()
        
        dfs([], s)
        return output