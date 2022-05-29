from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and stack[-1]>0 and asteroid<0:
                collision = stack[-1] + asteroid

                if collision < 0:
                    stack.pop()
                elif collision > 0:
                    break
                else:
                    stack.pop()
                    break
            else:
                stack.append(asteroid)
        return stack

print(Solution().asteroidCollision(asteroids = [5,10,-5]))
print(Solution().asteroidCollision(asteroids = [8,-8]))
print(Solution().asteroidCollision(asteroids = [10,2,-5]))
print(Solution().asteroidCollision(asteroids = [-2,-1,1,2]))