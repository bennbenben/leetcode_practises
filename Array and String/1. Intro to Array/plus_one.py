from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Get the large integer and increment it by one
        digits_str = str()
        for i in digits:
            digits_str+=str(i)
        increment_digits_str=str(int(digits_str)+1)

        # Iterate through the large integer and append it into a list
        increment_digits=list()
        for i in increment_digits_str:
            increment_digits.append(int(i))
        return increment_digits

# Driver code
s = Solution()
# Test case 1
print('Executing test case 1: digits = [1,2,3]')
print('Output for test case 1: {}'.format(s.plusOne(digits = [1,2,3])))
# Test case 2
print('Executing test case 2: digits = [4,3,2,1]')
print('Output for test case 2: {}'.format(s.plusOne(digits = [4,3,2,1])))
# Test case 3
print('Executing test case 3: digits = [9]')
print('Output for test case 3: {}'.format(s.plusOne(digits = [9])))
