from collections import Counter
import heapq

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter_nums = Counter(nums)
        heap_list = list()
        
        for key, val in counter_nums.items():
            heap_list.append((-val, key))
            
        heapq.heapify(heap_list)
        x = heapq.heappop(heap_list)[1]
        
        return x