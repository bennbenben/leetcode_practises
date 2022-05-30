class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_sum = 0
        prefix_sum_map = {0: 1}
        output = 0
        for n in nums:
            sub_sum += n
            diff = sub_sum - k

            output += prefix_sum_map.get(diff, 0)
            prefix_sum_map[sub_sum] = prefix_sum_map.get(sub_sum,0) + 1
            
        return output

# refer to https://www.youtube.com/watch?v=fFVZt-6sgyo&t=5s&ab_channel=NeetCode for explanation