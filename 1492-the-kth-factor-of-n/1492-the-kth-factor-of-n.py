class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        #Check all factors before sqrt and see if k becomes zero
        n_sqrt = int(math.sqrt(n))
        for f in range(1, n_sqrt+1):
            if n%f == 0:
                k-=1
            if k==0:
                return f
        
        factor_before_sqrt = n_sqrt if  n_sqrt*n_sqrt != n else n_sqrt-1
        
        #Start going back the same factors, and return the counterpart factors if k == 0
        for f in range(factor_before_sqrt,0,-1):
            if n%f == 0:
                k-=1
            if k == 0:
                return n//f
        
        return -1
            
            
        