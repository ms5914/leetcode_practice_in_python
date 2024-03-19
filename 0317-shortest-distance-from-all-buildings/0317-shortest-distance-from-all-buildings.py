class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        distance = [[0 for i in range(len(grid[0]))] for _ in range(len(grid))]
        reachable_buildings = [[0 for i in range(len(grid[0]))] for _ in range(len(grid))]
        total_buildings = 0
        
        
        def find_neighbors(i,j):
            dx = [0,0,1,-1]
            dy = [1,-1,0,0]
            for k in range(len(dx)):
                i1 = i+dx[k]
                j1 = j+dy[k]
                if i1>=0 and i1 < len(grid) and j1 >=0 and j1<len(grid[0]) and grid[i1][j1] == 0:
                    yield i1,j1
            
        def bfs(i,j, d):
            q = deque()
            visited = set()
            visited.add((i,j))
            q.append((i,j,d))
            while q:
                i,j, d = q.popleft()
                for i1, j1 in find_neighbors(i,j):
                    if not (i1,j1) in visited:
                        distance[i1][j1] += d+1
                        reachable_buildings[i1][j1]+=1
                        visited.add((i1, j1))
                        q.append((i1,j1,d+1))
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    total_buildings+=1
                    bfs(i,j, 0)
        
        ans = float('inf')
        # print(f"{reachable_buildings} are reacheable buildings")
        # print(f"{distance} are distance")
        
             
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and reachable_buildings[i][j] == total_buildings :
                    ans = min(ans, distance[i][j] )
        
        return ans if ans != float('inf') else -1
                    
        
            
            
            
        