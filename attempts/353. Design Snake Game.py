from collections import deque
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.q = deque()
        self.q.append([0,0])
        self.score = 0

    def move(self, direction: str) -> int:
        # get current head coordinates
        head_r, head_c = self.q[-1]
        
        # get new head coordinates
        if direction == "U":
            head_r -= 1
        elif direction == "R":
            head_c += 1
        elif direction == "D":
            head_r += 1
        elif direction == "L":
            head_c -= 1
        
        # check if new head coordinates are valid
        if not (head_r in range(self.height)) or not (head_c in range(self.width)):
            return -1 # snake collides with border
        
        # check if snake has moved to food
        if self.food and [head_r, head_c] == self.food[0]:
            self.food.pop(0) # remove 1 food
            self.q.append([head_r,head_c]) # add new snake head to the q
            self.score += 1
        # check if move is just a move (not eating food)
        else:
            self.q.popleft() # remove tail
            
            # check if snake eats himself
            if [head_r,head_c] in self.q:
                return -1 # snake eats himself
            else:
                self.q.append([head_r,head_c])
                
        return self.score

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)