class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # define variables
        plates_till_here,cumulative_plates = list(),0 # for prefix_sum
        nearest_right, right_candle = list(), -1 # for nearest right candle
        nearest_left, left_candle = list(), -1 # for nearest left candle
        output=[0]*len(queries)
        
        # create prefix sums
        for i in range(len(s)):
            if s[i] == "*":
                cumulative_plates += 1    
            plates_till_here.append(cumulative_plates)
        
        # nearest candle on index's right (left-iteration)
        for i in range(len(s)):
            if s[i] == "|":
                left_candle = i
            nearest_left.append(left_candle)
            
        # nearest candle on index's left (right-iteration)
        for i in range(len(s)-1, -1, -1):
            if s[i] == "|":
                right_candle = i
            nearest_right.append(right_candle)
        nearest_right = nearest_right[::-1]
        
        # iterate through queries
        for i, (left_index, right_index) in enumerate(queries):
            left_index = nearest_right[left_index]
            right_index = nearest_left[right_index]
            
            if left_index == -1 or right_index == -1 or (left_index >= right_index):
                continue
            
            prefix_plates = plates_till_here[right_index]-plates_till_here[left_index]
            output[i] = prefix_plates
        
        return output