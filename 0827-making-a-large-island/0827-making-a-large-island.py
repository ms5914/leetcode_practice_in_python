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
                while self.parent[coord] != coord:
                    coord = self.parent[coord]
                return coord
            
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
                            
        
                    
                
            
                
            
        