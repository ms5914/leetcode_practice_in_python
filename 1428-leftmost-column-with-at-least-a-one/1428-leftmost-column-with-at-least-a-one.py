# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        
        i,j = 0, n-1
        least_col = float('inf')
        
        while i<m and j>=0:
            if binaryMatrix.get(i,j) == 0:
                i+=1
            elif binaryMatrix.get(i,j) == 1:
                least_col = min(least_col, j)
                j-=1
        return least_col if least_col != float('inf') else -1
                
                
            
        