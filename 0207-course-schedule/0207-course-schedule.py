class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        #Method 2: Dfs to find cycles. Need to check if there are any back edges. See the added link for more explanation. The in_stack tracks whether a current node is in the stack currently being processed. 
        pre_list = [[] for i in range(numCourses)]
        for prereq in prerequisites:
            pre_list[prereq[1]].append(prereq[0])
            
        
        visited = set()
        in_stack = [False]*numCourses
        
        def dfs(n):
            # if n in visited: 
            #     if in_stack[n]:
            #         return True
            #     return False
            
            #Making it similar to dfs templates that I am going to use now
            visited.add(n)
            in_stack[n] = True
            for course in pre_list[n]:
                if course in visited and in_stack[course]:
                    return True
                elif course not in visited and dfs(course):
                    return True
            in_stack[n] = False
            return False
        
        for course in range(numCourses):
            if dfs(course):
                return False
        
        return True
                
            
                
        
        
     
    
    
#     #Method 1 : Top sort kinda
    
    
#     #Make a queue and add courses whose in_degree are 0 and then when those courses are added reduce the in_degrees of their neighbour courses i.e the courses that are dependent on them for their completion. Then add those neighbors in the queue whose in_degree have become zero. This is called Kahn's algorithm. It is used for topological sorting as well. 
        
#         pre_list = [[] for i in range(numCourses)]
#         in_degree = [0 for i in range(numCourses)]
    
#         for prereq in prerequisites:
#             pre_list[prereq[1]].append(prereq[0])
#             in_degree[prereq[0]]+=1
        
#         dq = deque()
#         visited = set() 
#         #We can do even without this set and just keeping the track of number of courses visited. This is an #optimization as two nodes won't be visited twice actually. We put a neighbor in queue if it's indegree becomes zero. 
#         #It won't be reached by any other node since it has already become zero and hence no need for visited. 
#         for i in range(len(in_degree)):
#             if in_degree[i] == 0:
#                 dq.append(i)
        
#         while dq:
#             course = dq.popleft()
#             visited.add(course)
            
#             for course in pre_list[course]:
#                 in_degree[course]-=1
#                 if in_degree[course] == 0 and not course in visited:
#                     dq.append(course)
        
#         return len(visited) == numCourses
    
    
    
#     #https://leetcode.com/problems/course-schedule/discuss/441722/Python-99-time-and-100-space.-Collection-of-solutions-with-explanation
            
            
            
            
            
            
        