class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        def dfs(i, j, word, visited, index):
            if index == len(word):
                return True
            visited.add((i,j))
            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]
            for k in range(len(dx)):
                new_x = i + dx[k]
                new_y = j+dy[k]
                if new_x >= 0 and new_x<m and new_y>=0 and new_y<n and not (new_x, new_y) in visited and board[new_x][new_y] == word[index]:
                    if dfs(new_x, new_y, word,visited, index+1):
                        return True
                    visited.remove((new_x, new_y)) #This is the backtracking part. We explored one path and didn't find a solution. We need to unset the visited nodes in this path. This is like DFS with backtracking. 
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = set()
                    if dfs(i,j,word, visited,1):
                        return True
        
        return False
    
        