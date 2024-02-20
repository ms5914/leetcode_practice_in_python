"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        parent = root
        while parent:
            dummy = Node(-1)
            current = dummy
            while parent:
                if parent.left:
                    current.next = parent.left
                    current = current.next
                if parent.right:
                    current.next = parent.right
                    current = current.next
                parent = parent.next
            parent = dummy.next
        return root
                
            
                
                
        