class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        if n<0:
            n = -1*n
            x = 1/x
            return self.myPow(x, n)
        if x == 1:
            return 1
        result = 1
        while n>0:
            if n%2 == 1:
                result*=x
            x = x*x
            n = n//2
        return result
                
            