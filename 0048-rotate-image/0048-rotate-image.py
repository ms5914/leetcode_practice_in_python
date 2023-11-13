class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for k in range(n//2):
            for i in range(k,n-k-1):
                tmp = matrix[i][n-k-1]
                matrix[i][n-k-1] = matrix[k][i]

                tmp1 = matrix[n-1-k][n-1-i]
                matrix[n-1-k][n-1-i] = tmp

                tmp2 = matrix[n-i-1][k]
                matrix[n-1-i][k]=tmp1
                
                matrix[k][i]=tmp2
            print(matrix)
        return matrix


