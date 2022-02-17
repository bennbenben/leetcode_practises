from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            extracted_num = nums.pop()
            nums.insert(0,extracted_num)
        # print(nums)

s = Solution()
print(s.rotate(nums = [1,2,3,4,5,6,7], k = 3))