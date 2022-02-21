from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_ptr = 0
        r_ptr = len(numbers)-1

        while l_ptr != r_ptr:
            current_sum = numbers[l_ptr] + numbers[r_ptr]

            if current_sum < target:
                l_ptr+=1
            elif current_sum > target:
                r_ptr-=1
            else:
                return [l_ptr+1, r_ptr+1]


# Driver code
s = Solution()
# Test case 1
print('Executing test case 1: numbers = [2,7,11,15], target = 9')
print('Output for test case 1: {}'.format(s.twoSum(numbers = [2,7,11,15], target = 9)))

# Test case 2
print('Executing test case 2: numbers = [2,3,4], target = 6')
print('Output for test case 2: {}'.format(s.twoSum(numbers = [2,3,4], target = 6)))

# Test case 3
print('Executing test case 3: numbers = [-1,0], target = -1')
print('Output for test case 3: {}'.format(s.twoSum(numbers = [-1,0], target = -1)))