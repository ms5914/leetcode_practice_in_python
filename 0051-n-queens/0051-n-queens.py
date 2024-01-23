class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:         
        li = [["." for _ in range(n)] for _ in range(n)]
        result = []
        #Use these sets to store the current state. i.e which rows have a quuen, which diags have queen, and which cols have a queen. 
        main_diag = set()
        cols = set()
        rows = set()
        anti_diag = set()
        
        def place_queen(li, row_num):
            if row_num == n:
                result.append(["".join(row_places) for row_places in li])
            else:
                for col_num in range(n):
                    if isValid(li,row_num,col_num):
                        
                        #To compute the current diagonal number using row and col
                        main_diagonal = col_num-row_num #top left to bottom right
                        
                        anti_diagonal = row_num+col_num #Top right to bottowm left
                        li[row_num][col_num]="Q"
                        rows.add(row_num)
                        cols.add(col_num)
                        main_diag.add(main_diagonal)
                        anti_diag.add(anti_diagonal)
                        place_queen(li, row_num+1)
                        li[row_num][col_num]="."
                        rows.remove(row_num)
                        cols.remove(col_num)
                        main_diag.remove(main_diagonal)
                        anti_diag.remove(anti_diagonal)
        
        def isValid(li, row, col):
            if row in rows or col in cols or col-row in main_diag or row+col in anti_diag:
                return False
            return True
            
        
            
        place_queen(li, 0)
        return result
        
        #TC : About O(N!) . We can place queen in N cols in first row, N-2 (Don't consider col used in prev row and any col directly left or right of it) cols in second row and so on. 
        # While it costs O(N^2) to build each valid solution , the amount of valid solutions S(N) doesn't grow as nearly as N!, so O(N! + S(N)*N^2) = O(N!)
        
        #SC: O(N^2) to store board state. result space is not counted
            
                
        