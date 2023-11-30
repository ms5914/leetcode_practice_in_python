class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        count = 0
        def bfs(i,j):
            q = deque()
            q.append((i,j))
            grid[i][j]="0"
            while q:
                (i,j) = q.popleft()
                dx, dy = [0, 0, 1, -1], [1,-1,0,0]
                for k in range(len(dx)):
                    new_i = i+dx[k]
                    new_j = j+dy[k]
                    if new_i>=0 and new_i<m and new_j>=0 and new_j<n and grid[new_i][new_j] == "1":
                        q.append((new_i, new_j))
                        grid[new_i][new_j]="0" #set visited here to avoid duplicates and TLE
                        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count+=1
                    bfs(i,j)
        
        return count
        
                    
                    
        