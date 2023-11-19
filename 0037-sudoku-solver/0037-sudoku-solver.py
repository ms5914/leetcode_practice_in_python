class Solution(object):
    def solveSudoku(self, matrix):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n = len(matrix)
        row_tracker = [set() for _ in range(n) ]
        col_tracker = [set() for _ in range(n) ]
        box_tracker = [set() for _ in range(n) ]
        
        for i in range(n):
            for j in range(n):
                if matrix[i][j] !=".":
                    row_tracker[i].add(int(matrix[i][j]))
                    col_tracker[j].add(int(matrix[i][j]))
                    box_tracker[(i//3)*3+j//3].add(int(matrix[i][j]))
        
        def backtrack(i, j):
            if matrix[i][j] == ".":
                for num in range(1,10):
                    if num not in row_tracker[i] and num not in col_tracker[j] and num not in box_tracker[(i//3)*3+j//3]:
                        matrix[i][j] = str(num)
                        row_tracker[i].add(num)
                        col_tracker[j].add(num)
                        box_tracker[(i//3)*3+j//3].add(num)
                        if i == n-1 and j==n-1:
                            return True
                        elif j<n-1:
                            if backtrack(i,j+1):
                                return True
                        elif j == n-1:
                            if backtrack(i+1,0):
                                return True
                        matrix[i][j] = "."
                        row_tracker[i].remove(num)
                        col_tracker[j].remove(num)
                        box_tracker[(i//3)*3+j//3].remove(num)
                return False
            else:
                if i == n-1 and j==n-1:
                    return True
                elif j<n-1:
                    if backtrack(i,j+1):
                        return True
                elif j == n-1:
                    if backtrack(i+1,0):
                        return True
                return False
                    
        backtrack(0,0)        
                
                    
                    
                    
                    
                    
        