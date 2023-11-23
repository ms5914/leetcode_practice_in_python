"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hm = {}
        if not node:
            return None
        
        hm[node] = Node(node.val, [])
        
        def dfs(node, hm):
            for neighbor in node.neighbors:
                if not neighbor in hm:
                    hm[neighbor] = Node(neighbor.val, [])
                    dfs(neighbor, hm)
                hm[node].neighbors.append(hm[neighbor])
    
        dfs(node, hm)  
        return hm[node]

                    
            
    
                    
                            
                
                