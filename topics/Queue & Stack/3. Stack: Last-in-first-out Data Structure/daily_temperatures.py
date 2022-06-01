from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        warmer_day = [0]*len(temperatures)

        for i, day_temp in enumerate(temperatures):
            while stack and stack[-1][0] < day_temp:
                prev_temp, prev_day = stack.pop()
                warmer_day[prev_day] = i-prev_day
            stack.append((day_temp, i))

        return warmer_day

s = Solution()
res = s.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73])
print(res)