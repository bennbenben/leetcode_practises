from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and asteroid<0 and stack[-1]>0:
                collision = stack[-1] + asteroid

                if collision > 0:
                    asteroid=0
                elif collision < 0:
                    stack.pop()
                else:
                    asteroid=0
                    stack.pop()

            if asteroid != 0:
                stack.append(asteroid)
        return stack

print(Solution().asteroidCollision(asteroids = [5,10,-5]))
print(Solution().asteroidCollision(asteroids = [8,-8]))
print(Solution().asteroidCollision(asteroids = [10,2,-5]))
print(Solution().asteroidCollision(asteroids = [-2,-1,1,2]))
