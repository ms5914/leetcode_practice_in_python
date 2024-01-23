class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:         
        li = [["." for _ in range(n)] for _ in range(n)]
        result = []
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
                        main_diagonal = col_num-row_num
                        anti_diagonal = row_num+col_num
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
                
            
                
        