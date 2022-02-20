class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Reverse the string digits because ord() function only takes in one character
        rev_a,rev_b=a[::-1],b[::-1]
        carry,output=0,""

        for i in range(max(len(a),len(b))):

            if i < len(a):
                digit_a=ord(rev_a[i]) - ord("0")
            else:
                digit_a=0
            if i < len(b):
                digit_b=ord(rev_b[i]) - ord("0")
            else:
                digit_b=0

            total = digit_a+digit_b+carry
            output = str(total%2) + output
            carry = total//2

        if carry:
            output = "1" + output
        return output



# Driver code
s = Solution()
# Test case 1
print('Executing test case 1: a = "11", b = "1"')
print('Output for test case 1: {}'.format(s.addBinary(a = "11", b = "1")))

# Test case 2
print('Executing test case 2: a = "1010", b = "1011"')
print('Output for test case 2: {}'.format(s.addBinary(a = "1010", b = "1011")))
