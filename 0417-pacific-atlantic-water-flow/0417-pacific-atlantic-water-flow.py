class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        
        pacific = [[False for i in range(m)] for j in range(n)]
        atlantic = [[False for i in range(m)] for j in range(n)]
        result = []
        
        pacific_visited = set()
        atlantic_visited = set()
        
        def bfs(visited, ocean):
            q = deque()
            if ocean == "pacific":
                for i in range(m):
                    q.append((i,0))
                    visited.add((i,0))
                for j in range(1, n):
                    q.append((0,j))
                    visited.add((0,j))
            else:
                for i in range(m):
                    q.append((i,n-1))
                    visited.add((i,n-1))
                for j in range(0, n-1):
                    q.append((m-1,j))
                    visited.add((m-1,j))

            while q:
                (x, y) = q.popleft()
                dx = [1, -1, 0, 0]
                dy = [0, 0, 1, -1]
                for k in range(len(dx)):
                    new_i = x+dx[k]
                    new_j = y+dy[k]
                    if new_i >= 0 and new_i<m and new_j>=0 and new_j<n and not (new_i, new_j) in visited and heights[new_i][new_j]>=heights[x][y]:
                        visited.add((new_i, new_j))
                        q.append((new_i, new_j))
                    
        bfs(pacific_visited, "pacific")
        bfs(atlantic_visited, "atlantic")
        
        for pair in pacific_visited:
            if pair in atlantic_visited:
                result.append([pair[0], pair[1]])
        
        return result
        