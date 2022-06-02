class Solution:
    def maximumSwap(self, num: int) -> int:
        list_num = list(str(num))
        max_nums = num
        
        for i in range(len(list_num)):
            for j in range(i+1, len(list_num)):
                swapped_nums = list_num.copy()
                swapped_nums[i], swapped_nums[j] = swapped_nums[j], swapped_nums[i]
                max_nums = max(max_nums, int("".join(swapped_nums)))
                
        return max_nums