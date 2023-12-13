class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        start_x, start_y = 0,0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "*":
                    start_x = i
                    start_y = j
                    
        visited = set()
        q = deque()
        
        q.append((start_x,start_y,0))
        visited.add((start_x,start_y))
        
        while q:
            i, j, steps = q.popleft()
            if grid[i][j] == "#":
                return steps
            else:
                dx = [1, -1, 0, 0]
                dy = [0, 0, 1, -1]
                for k in range(len(dx)):
                    new_i = i+dx[k]
                    new_j = j+dy[k]
                    if new_i >= 0 and new_i<m and new_j>=0 and new_j<n and not (new_i, new_j) in visited and grid[new_i][new_j]!="X":
                        visited.add((new_i, new_j))
                        q.append((new_i, new_j, steps+1))
        return -1
            
        
                    