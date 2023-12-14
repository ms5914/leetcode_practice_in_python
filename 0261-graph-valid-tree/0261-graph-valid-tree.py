class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        
        for i,j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
        
        
        visited = set()
        def dfs(start, parent):
            visited.add(start)
            
            for node in adjList[start]:
                if node in visited: 
                    if node != parent:  #This is to make sure that we are not looking at a "trivial cycle" (edge back to parent) : Common in undirected graphs. One another approach is that we remove the back edge to parent once we see a neighbor. 
                        return True
                else:
                    if dfs(node, start):
                        return True
            return False
        
        has_cycle = dfs(0, -1)
        return not has_cycle and len(visited) == n
                
        #Don't forget to read the solution editorial https://leetcode.com/problems/graph-valid-tree/solution/
        #for this one. It's very good 
        
        #There are two more ways to do it: 
        #1. First is that if a graph contains excatly N-1 edges (n=num of nodes) and is FULLY CONNECTED -> It's a valid tree
        # N-1 edges csn be checked easilt in the beginning , for fully connected just do a DFS/BFS and check then length of visited set
        
        
        #2. Union find -> same logic as above, we can check the number of edges easily. For connected components, starightforward way is to see that there is only one component. However we can stop early. If any find operation doesn't lead to a new merge, that means there's an edge that is repeated. i.e two vertices already had some path (they are in same set) and we are adding an edge that is creating one more path between them so this isn't a valid tree.   
        
            
            
        