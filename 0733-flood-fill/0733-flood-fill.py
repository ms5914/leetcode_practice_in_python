class Solution:
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.m = len(image)
        self.n = len(image[0])
        self.visited = [[False]*self.n for _ in range(self.m)]
        self.fill_color(sr, sc, image, color)
        return image
    
    
    def fill_color(self, sr, sc, image, color):
        self.visited[sr][sc] = True
        
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        
        for i in range(len(dx)):
            new_sr = sr+dx[i]
            new_sc = sc + dy[i]
            
            if new_sr<self.m and new_sr>=0 and new_sc<self.n and new_sc>=0 and not self.visited[new_sr][new_sc] and image[new_sr][new_sc] == image[sr][sc]:
                self.fill_color(new_sr,new_sc, image, color)
        image[sr][sc]=color
    
    