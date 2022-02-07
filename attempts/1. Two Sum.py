class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d_comps=dict()
        
        for i in range(len(nums)):
            num = nums[i]
            comp = target - num
            
            if num in d_comps:
                return [d_comps[num],i]
            else:
                d_comps[comp] = i