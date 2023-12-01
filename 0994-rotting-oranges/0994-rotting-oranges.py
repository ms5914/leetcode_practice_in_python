class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        q = deque()
        min_minutes = 0
        
        fresh_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i,j,0])
                elif grid[i][j] == 1:
                    fresh_count+=1
                    
        while q:
            i,j,minutes = q.popleft()
            min_minutes = max(min_minutes, minutes)
            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]
            
            for k in range(len(dx)):
                new_x = i + dx[k]
                new_y = j + dy[k]
                if new_x>=0 and new_x<m and new_y>=0 and new_y<n and grid[new_x][new_y]==1:
                    
                    fresh_count-=1
                    grid[new_x][new_y] = 2
                    q.append([new_x, new_y, minutes+1])
            
        if fresh_count == 0:
            return min_minutes
        else:
            return -1
        
        # if  all (list(grid[p][q] in (0,2) for p in range(m) for q in range(n))):
        #     return min_minutes
        # else:
        #     return -1
        
        
        
        
                
            
            
            
        
        
            
        
        
                
        