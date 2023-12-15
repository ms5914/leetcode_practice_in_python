class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Direct application of topological sorting Kahn's algorithm
        
        
        
        adjList = defaultdict(list)
        in_edges = defaultdict(int)
        for course in range(numCourses):
            in_edges[course] = 0
            
        
        for a,b in prerequisites:
            adjList[b].append(a) #Directed graph
            in_edges[a]+=1
        
        
        q = deque()
        for course in range(numCourses):
            if in_edges[course] == 0:
                q.append(course)
        
        result = []
        
        while q:
            pre_req = q.popleft()
            result.append(pre_req)
            
            for course in adjList[pre_req]:
                in_edges[course]-=1
                if in_edges[course] == 0:
                    q.append(course)
        
        return result if len(result) == numCourses else [] 
                
            
                
                
            
            
            
            
            
            
        