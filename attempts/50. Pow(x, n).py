class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            # recursive base case
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            # recursion calls
            result = helper(x, n//2) # recursive call. 2^10 will return 2^5
            result = result * result # merge recursive calls. 2^5 x 2^5 = 2^10
            
            # handle odd number case
            if (n % 2 != 0):
                result = result * x
            
            return result
        
        
        output = helper(x,abs(n))
        
        if (n < 0):
            output = 1/output
        
        return output