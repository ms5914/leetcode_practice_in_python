class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_tracker = [[0]*9 for _ in range(9)]
        col_tracker = [[0]*9 for _ in range(9)]
        box_tracker = [[0]*9 for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!=".":
                    index = ord(board[i][j])-ord("0")-1
                    if row_tracker[i][index] == 1:
                        return False
                    if col_tracker[j][index] == 1:
                        return False
                    box_index = ((i//3)*3)+(j//3)
                    if box_tracker[box_index][index] == 1:
                        return False

                    row_tracker[i][index] = 1
                    col_tracker[j][index] = 1
                    box_tracker[box_index][index] = 1
        
        return True

                    

        
        