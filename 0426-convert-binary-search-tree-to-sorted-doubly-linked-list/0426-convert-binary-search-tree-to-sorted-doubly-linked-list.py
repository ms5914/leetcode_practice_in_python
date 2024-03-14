"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
         
        dummy = Node(-1)
        last = dummy
        
        def traverse_tree(node):
            nonlocal last
            if not node:
                return
            traverse_tree(node.left)
            last.right = node
            node.left = last
            last = node
            traverse_tree(node.right)
        
        
        traverse_tree(root)
        last.right = dummy.right
        dummy.right.left = last
        
        return dummy.right
            
            
            
            
        
        
        