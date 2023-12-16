class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        if not n:
            return 0
        adjList = defaultdict(list)
        
        #Remember it's directed graph bro
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        
        visited = set()
        k = 0
        
        
        def dfs(node):
            visited.add(node)
            for neighbor in adjList[node]:
                if not neighbor in visited:
                    dfs(neighbor)
                    
        for i in range(n):
            if not i in visited:
                k+=1
                dfs(i)
        
        return k
        
        
        
        
                
            
        