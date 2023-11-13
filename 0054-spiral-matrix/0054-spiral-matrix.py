class Solution(object):
    def spiralOrder(self, matrix):


        #Intelligent solution
        # return matrix and list(matrix.pop(0)) + self.spiralOrder(list(zip(*matrix))[::-1])

        m,n = len(matrix)-1, len(matrix[0])-1
        up, down, left, right = 0, m, 0, n
        result=[]

        while len(result)<(m+1)*(n+1):
            for i in range(left, right+1, 1):
                    result.append(matrix[up][i])

            for i in range(up+1, down+1, 1 ):
                    result.append(matrix[i][right])

            #Checking if we are not repeating the same row in case of horizontal matrix like this [[1,3,4,5]] or towards the end when we are in the mid of the matrix
            if up!=down:
                for i in range(right-1, left-1, -1):
                    result.append(matrix[down][i])
                       #Checking if we are not repeating the same column in case of horizontal matrix like this [[1],[3],[4],[5]] or towards the end when we are in the mid of the matrix.
            if left!=right:
                for i in range(down-1, up, -1):
                    result.append(matrix[i][left])
            
            left+=1
            right-=1
            up+=1
            down-=1

        return result






            



