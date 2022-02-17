class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result=""
        carry=0

        a,b = a[::-1], b[::-1]

        for i in range(max(len(a),len(b))):

            if i<len(a):
                digit_a = ord(a[i]) - ord("0")
            else:
                digit_a=0
            if i<len(b):
                digit_b = ord(b[i]) - ord("0")
            else:
                digit_b=0

            total = digit_a+digit_b+carry
            result = str(total%2) + result
            carry = total//2

        if carry:
            result = "1" + result

        return result

s = Solution()
print(s.addBinary(a="11",b="1"))