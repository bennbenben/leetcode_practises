class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0
        
        while left < right:
            # compute area for the given dimensions
            length = right - left
            breadth = min(height[left], height[right])
            area = length * breadth
            
            # update max area
            max_area = max(max_area, area)
            
            # get next iteration
            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else: # does not matter which pointer shifts
                right -= 1

        return max_area