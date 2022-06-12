class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        q = deque()
        count = 0
        
        for char in s:
            while q and q[-1] == char and q[0] != char:
                q.pop()
            if q and q[-1] != char:
                q.pop()
                count += 1
            q.appendleft(char)
        return count