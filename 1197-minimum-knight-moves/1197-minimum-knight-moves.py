class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x ==0 and y==0: #This base case is important
            return 0
        

        
       
        
        #Solution 1 : Straightforward BFS
#         visited = set()
#         q = deque()
#         q.append((0,0,0))
#         visited.add((0,0))

#         while q:
#             dest_x, dest_y, step = q.popleft()
#             dx = [2, 2, -2, -2, 1, -1, 1, -1]
#             dy = [1, -1, 1, -1, 2, 2, -2, -2]

#             for k in range(len(dx)):
#                 new_x = dest_x+dx[k]
#                 new_y = dest_y + dy[k]

#                 if not (new_x, new_y) in visited:
#                     if (new_x, new_y) == (x,y):  #In BFS always check here. In DFS check above when you pop elements
#                         return step+1
#                     visited.add((new_x, new_y))
#                     q.append((new_x, new_y, step+1))
        
        
        
        
        #Solution 2 : Bidirectional BFS: Whenever you see a cell (in forward/backward traversal) that has already been visited by in other_visited. You have found the path. Visited is a dictionary which stores step to a particular cell from origin (forward bfs) or (x,y) (backwards bfs) 
#         dx = [2, 2, -2, -2, 1, -1, 1, -1]  #Instead of initializing this again and again in the loop, initialize it here. 
#         dy = [1, -1, 1, -1, 2, 2, -2, -2]
        
        
        
#         def bfs(q, visited, other_visited):
#             for i in range(len(q)):
#                 dest_x, dest_y= q.popleft()
#                 for k in range(len(dx)):
#                     new_x = dest_x+dx[k]
#                     new_y = dest_y + dy[k]

#                     if not (new_x, new_y) in visited:
#                         if (new_x, new_y) in other_visited:
#                             return visited[(dest_x, dest_y)]+1+other_visited[(new_x, new_y)]
#                         visited[(new_x, new_y)] = visited[(dest_x, dest_y)]+1
#                         q.append((new_x, new_y))
#             return -1
        
#         forward_queue = deque([(0,0)])
#         forward_visited = {(0,0):0}
        
#         backward_queue = deque([(x,y)])
#         backward_visited = {(x,y):0}
        
#         even = True
#         while forward_queue and backward_queue:
#             if even:
#                 even = False
#                 res =  bfs(forward_queue, forward_visited, backward_visited)
#                 if res !=-1:
#                     return res
#             else:
#                 even = True
#                 res =  bfs(backward_queue, backward_visited, forward_visited)
#                 if res !=-1:
#                     return res


#Solution 3 : 
#DFS (recursion)
        #Reverse from x,y to 0,0 : Consider only first quadrant as answers are same across symmetries. Therefore use of abs
        @lru_cache(maxsize=None)
        def dfs(x,y):
            if x == 0 and y ==0:
                return 0
            elif x+y == 2: #(1,1),  (0,2), (2,0) 
                return 2
            else:
                return min(dfs(abs(x-1), abs(y-2)), dfs(abs(x-2), abs(y-1)))+1
        return dfs(abs(x),abs(y))



    
        
                    
                
            
        
        
            
                 
        
        
        