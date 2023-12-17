class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m,n = len(matrix), len(matrix[0])
        if not matrix:
            return 0
        
        delta = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        dp = [[0 for i in range(200)] for j in range(200)]
        
        
        def dfs(i,j):
            if dp[i][j]:
                return dp[i][j]
            max_path = 1
            for k in range(len(delta)):
                new_x = i+delta[k][0]
                new_y = j+delta[k][1]
                if new_x >= 0 and new_x < m and new_y >=0 and new_y <n and matrix[new_x][new_y]>matrix[i][j]:
                    max_path = max(max_path,dfs(new_x, new_y)+1)
            dp[i][j] = max_path
            return max_path
        
        ans = 1
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i,j))
                
        
        return ans
                
                    
                    
            
            