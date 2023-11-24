"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

#Both the DFS and BFS ways work
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hm = {}
        if not node:
            return None
        
        # hm[node] = Node(node.val, [])
        
#         DFS solution
#         def dfs(node, hm):
#             for neighbor in node.neighbors:
#                 if not neighbor in hm:
#                     hm[neighbor] = Node(neighbor.val, [])
#                     dfs(neighbor, hm)
#                 hm[node].neighbors.append(hm[neighbor])
    
#         dfs(node, hm)  

        #BFS Solution 
        q = deque()
        q.append(node)
        hm[node] = Node(node.val, [])
        while q:
            root = q.pop()
            for neighbor in root.neighbors:
                if neighbor not in hm:
                    hm[neighbor] = Node(neighbor.val, [])
                    q.append(neighbor)
                
                hm[root].neighbors.append(hm[neighbor])
        return hm[node]

                    
            
    
                    
                            
                
                