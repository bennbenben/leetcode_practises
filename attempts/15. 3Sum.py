from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        output = []
        output_list = list()
        
        for i in range(len(sorted_nums)):
            if i > 0 and i < len(sorted_nums) and sorted_nums[i] == sorted_nums[i-1]:
                continue
            
            left, right = i+1, len(sorted_nums)-1
            
            while left < right:
                three_sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    output.append([sorted_nums[i],sorted_nums[left],sorted_nums[right]])
                    left += 1
        for i in output:
            if i not in output_list:
                output_list.append(i)
        return output_list

s = Solution()
print(s.threeSum(nums = [-1,0,1,2,-1,-4]))