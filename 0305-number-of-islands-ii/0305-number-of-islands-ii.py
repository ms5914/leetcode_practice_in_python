class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        
        udj = Udj(m,n)
        result = []
        
        for c in map(tuple, positions):
            udj.add_coordinate(c)
            result.append(udj.num_islands)
            
        return result
            
              
class Udj:
    def __init__(self, m, n):
        self.mapp = {}
        self.num_islands = 0
        self.m = m
        self.n = n
    
    def validate_neighbor_island(self, c1_x, c1_y):
        if c1_x>=0 and c1_y>=0 and c1_x<self.m and c1_y<self.n and (c1_x, c1_y) in self.mapp:
            return True
        return False
        
    
    def find(self,c):
        while self.mapp[c] != c:
            c = self.mapp[c]
        return c
    
    def add_coordinate(self,c):
        if c in self.mapp:
            return 
        else:
            
            #Just add it
            self.num_islands+=1
            self.mapp[c] = c
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            
            for i in range(len(dx)):
                c1_x = c[0]+dx[i]
                c1_y = c[1]+dy[i]
                
                #Join with valid island neighbors now
                if self.validate_neighbor_island(c1_x, c1_y):
                    c1 = (c1_x, c1_y)
                    self.join(c, c1)
    
    def join(self, c1, c2):
        p1 = self.find(c1)
        p2 = self.find(c2)
        
        
        #if different parent, means combining to islands, hence reduce num_islands
        if p1!=p2:
            self.mapp[p1] = p2
            self.num_islands-=1
    
            
            
    
            

        
        
        
        
    
        