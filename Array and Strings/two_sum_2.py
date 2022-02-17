from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_ptr=0
        r_ptr=len(numbers)-1

        while l_ptr != r_ptr:
            current_sum = numbers[l_ptr]+numbers[r_ptr]

            if current_sum < target:
                l_ptr+=1
            elif current_sum > target:
                r_ptr-=1
            else:
                return [l_ptr+1, r_ptr+1]


s = Solution()
print(s.twoSum(numbers = [2,7,11,15], target = 9))