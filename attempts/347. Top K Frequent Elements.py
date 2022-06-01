# using data structure - heap
from typing import List
import heapq
from collections import Counter
class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		dict_counts = Counter(nums)
		max_heap = list()
		output = list()

		for key, val in dict_counts.items():
			max_heap.append((-val,key))

		heapq.heapify(max_heap)
		for i in range(k):
			output.append(heapq.heappop(max_heap)[1])
		return output

# using python libraries
from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums).most_common()
        output = list()

        for i in freq_map:
        	output.append(i[0])

        return output[:k]

print(Solution().topKFrequent(nums = [1,1,1,2,2,3], k=2))