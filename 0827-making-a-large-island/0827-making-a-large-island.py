class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        class dsu:
            def __init__(self):
                self.parent = {}
                self.parent_members = {}
                
            def find_count(self, coord):
                p1 = self.find_parent(coord)
                return self.parent_members[p1]
            
            def maximum_member_island_count(self):
                return max(list(self.parent_members.values())+[0])
                
            def add_member(self, coord):
                self.parent[coord] = coord
                self.parent_members[coord] = 1
            
            def find_parent(self, coord):
                coord1 = coord
                while self.parent[coord1] != coord1:
                    coord1 = self.parent[coord1]
                self.parent[coord] = coord1
                return coord1
            
            def union(self, coord1, coord2):
                p1 = self.find_parent(coord1)
                p2 = self.find_parent(coord2)
                if p1 != p2:
                    self.parent[p2] = p1
                    self.parent_members[p1]+=self.parent_members[p2]
            
        ds = dsu()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ds.add_member((i,j))
        
        delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for dx, dy in delta:
                        new_x = i+dx
                        new_y = j+dy
                        if new_x>=0 and new_x<len(grid) and new_y>=0 and new_y<len(grid[0]) and grid[new_x][new_y] == 1:        
                            
                            ds.union((i,j), (new_x, new_y))
        
                    
        max_island = 0          
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    result = 1
                    unique_islands = set()
                    for dx, dy in delta:
                        new_x = i+dx
                        new_y = j+dy
                        if new_x>=0 and new_x<len(grid) and new_y>=0 and new_y<len(grid[0]) and grid[new_x][new_y] == 1:            
                            p1 = ds.find_parent((new_x,new_y))
                            unique_islands.add(p1)
                    for element in unique_islands:
                        result = result + ds.find_count(element)
                        
                    max_island = max(max_island, result)
        
        
        return max(max_island, ds.maximum_member_island_count())
                            
        
                    
                
            #Solution 2: Intelligent way of marking every island by a particular number Ex.

# 0000
# 2200
# 0003
#There are two islands marked with integers 2 and 3 and also record the number of elements in those islands in a dictionary. 



# class Solution(object):
#     def largestIsland(self, grid):
#         N = len(grid)

#         def neighbors(r, c):
#             for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
#                 if 0 <= nr < N and 0 <= nc < N:
#                     yield nr, nc

#         def dfs(r, c, index):
#             ans = 1
#             grid[r][c] = index
#             for nr, nc in neighbors(r, c):
#                 if grid[nr][nc] == 1:
#                     ans += dfs(nr, nc, index)
#             return ans

#         area = {}
#         index = 2
#         for r in xrange(N):
#             for c in xrange(N):
#                 if grid[r][c] == 1:
#                     area[index] = dfs(r, c, index)
#                     index += 1

#         ans = max(area.values() or [0])
#         for r in xrange(N):
#             for c in xrange(N):
#                 if grid[r][c] == 0:
#                     seen = {grid[nr][nc] for nr, nc in neighbors(r, c) if grid[nr][nc] > 1}
#                     ans = max(ans, 1 + sum(area[i] for i in seen))
#         return ans
                
            
        