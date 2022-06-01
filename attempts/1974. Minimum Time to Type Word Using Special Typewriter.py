class Solution:
    def directions(self, letter, next_letter):
        forward = abs(ord(letter) - ord(next_letter))
        other_direction = 26 - forward
        return min(forward, other_direction)
        
    def minTimeToType(self, word: str) -> int:
        timer = int(len(word))
        timer = timer + self.directions('a', word[0])
        
        for i in range(1, len(word)):
            timer += self.directions(word[i], word[i-1])
        
        return timer

class Solution:
    def check_direction(self, nums):
        alt_direction = 26 - abs(nums)
        return min(alt_direction, abs(nums))
        
    def minTimeToType(self, word: str) -> int:
        dist_seconds = self.check_direction(ord(word[0])-ord('a'))
        
        for i in range(1,len(word)):
            dist = ord(word[i-1])-ord(word[i])
            dist_seconds += self.check_direction(dist)
        
        dist_seconds += len(word)
        return dist_seconds