class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        is_col_zero = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                is_col_zero = True
                break
        
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                matrix[0][0] = 0
                break
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(0, len(matrix[0])):
                    matrix[i][j] = 0
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(0, len(matrix)):
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        
        if is_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        
            
                    
                
            
        