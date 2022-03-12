from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        q = deque()
        q.append("0000")
        visited = set(deadends)

        turns=0

        def create_combis(combi):
            combinations=list()
            for i in range(4):
                digit = str((int(combi[i])+1)%10)
                inc_combi = combi[:i] + digit + combi[i+1:]
                combinations.append(inc_combi)

                digit = str((int(combi[i])-1)%10)
                dec_combi = combi[:i] + digit + combi[i+1:]
                combinations.append(dec_combi)
            return combinations

        while q:
            for _ in range(len(q)):
                combi = q.popleft()

                if combi == target:
                    return turns

                else:
                    child_combis = create_combis(combi)
                    for i in child_combis:
                        if i not in visited:
                            visited.add(i)
                            q.append(i)
            turns += 1
        return -1

s = Solution()
s_res = s.openLock(deadends=["0201","0101","0102","1212","2002"],target="0202")
print(s_res)
