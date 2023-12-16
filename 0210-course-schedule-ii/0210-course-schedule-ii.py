class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Solution 1: Direct application of topological sorting Kahn's algorithm
        
        
        
#         adjList = defaultdict(list)
#         in_edges = defaultdict(int)
#         for course in range(numCourses):                #You forgot this and missed out on edge case. For ex. there are no depedencies. Then in_edges should be explicitly set zero
#             in_edges[course] = 0
            
        
#         for a,b in prerequisites:
#             adjList[b].append(a) #Directed graph
#             in_edges[a]+=1
        
        
#         q = deque()
#         for course in range(numCourses):                    #You should loop for all possible courses and not just the adjacency list
#             if in_edges[course] == 0:
#                 q.append(course)
        
#         result = []
        
#         while q:
#             pre_req = q.popleft()
#             result.append(pre_req)
            
#             for course in adjList[pre_req]:
#                 in_edges[course]-=1
#                 if in_edges[course] == 0:
#                     q.append(course)
        
#         return result if len(result) == numCourses else [] 
        
        
        #Solution 2: Can be done using recursion also. See Editorial
        # The way DFS would work is that we would consider all possible paths stemming from A before finishing up the recursion for A and moving onto other nodes. All the nodes in the paths stemming from the node A would have A as an ancestor. The way this fits in our problem is, all the courses in the paths stemming from the course A would have A as a prerequisite.
        
        result = []
        if numCourses == 0:
            return result
        
        visited = set()
                
        adjList = defaultdict(list)
        for edge in prerequisites:
            adjList[edge[1]].append(edge[0])
            
        has_cycle = False
            
        exploring = set()
        
        def dfs(prereq):
            nonlocal has_cycle
            if has_cycle: 
                return -1
            visited.add(prereq)
            exploring.add(prereq)
            for course in adjList[prereq]:
                if course in exploring:
                    has_cycle = True
                if not course in visited: 
                    dfs(course)
            exploring.remove(prereq)
            result.append(prereq)
         
        for course in range(numCourses):
            if not course in visited:
                ret_val = dfs(course)
                if has_cycle:
                    return []

        return result[::-1]
    
    
    #Detecting cycles in directed and undirected graphs is different:
    #1. In undirected graphs: a normal check for whether a neighbor has already been visited will suffice
    #2. In directed graph you have to check whether you are back to a parent node that you are currently still exploring. This question uses that approach. 
    #3. There is a difference between visited and exploring. Exploring means you are still in the same hierarchy. Visited can be from a different hierarchy. Visiting a node already doesn't necessarily mean a loop in directed graph
    #4, Ex. (1,2) (1,3) (3,2) : This is a loop in undirected graph but not in directed graph
        
        
            
        
        
        
        
            
            
            
        
        
            
        
        
        
        
                
                
            
            
            
            
            
            
        