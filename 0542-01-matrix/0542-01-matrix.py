class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        #Using multi-source bfs from 0s as start index
        #The concept is that the closest zero to a one will reach it first
        #The depth it has traversed to reach that 1 is the shortest distance of that zero from 1
        
        #BFS approach
        
#         q = deque()
#         visited = set()
#         for i in range(len(mat)):
#             for j in range(len(mat[0])):
#                 if mat[i][j] == 0:
#                     q.append([i,j,0])
#                     visited.add((i,j))
                    
        
#         while q:
#             i,j, level = q.popleft()
#             mat[i][j] = level
            
#             dx = [0,0,1,-1]
#             dy = [1,-1,0,0]
            
#             for k in range(len(dx)):
#                 new_i = i+dx[k]
#                 new_j = j+dy[k]
                
#                 if new_i>=0 and new_i<len(mat) and new_j>=0 and new_j<len(mat[0]) and mat[new_i][new_j] == 1 and not (new_i,new_j) in visited:
#                     visited.add((new_i,new_j))
#                     q.append([new_i, new_j, level+1])
        
#         return mat




#DP (2 way DP) approach
    
        

         
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    mat[i][j] = float("inf")
                    
                
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] != 0:
                    if i>0:
                        mat[i][j] = min(mat[i][j], mat[i-1][j]+1)
                    if j>0:
                        mat[i][j] = min(mat[i][j], mat[i][j-1]+1)
                        
        
        for i in range(len(mat)-1, -1, -1):
            for j in range(len(mat[0])-1, -1, -1):
                if i<len(mat)-1:
                    mat[i][j] = min(mat[i][j], mat[i+1][j]+1)
                
                if j<len(mat[0])-1:
                    mat[i][j] = min(mat[i][j], mat[i][j+1]+1)
        
        return mat
                    
                    
                    
            
        
        
                        
        
        
                    
    
    
    