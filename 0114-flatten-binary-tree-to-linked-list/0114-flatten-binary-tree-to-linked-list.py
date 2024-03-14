# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        
        """
        
        if not root:
            return
        l,r = self.flatten(root.left), self.flatten(root.right)
        curr = root
        if l:
            curr.right = l
            while curr.right:
                curr = curr.right
            curr.right = r
            root.left = None
        return root
        
        #Morris traversal technique\
        
#         class Solution:
    
#     def flatten(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
        
#         # Handle the null scenario
#         if not root:
#             return None
        
#         node = root
#         while node:
            
#             # If the node has a left child
#             if node.left:
                
#                 # Find the rightmost node
#                 rightmost = node.left
#                 while rightmost.right:
#                     rightmost = rightmost.right
                
#                 # rewire the connections
#                 rightmost.right = node.right
#                 node.right = node.left
#                 node.left = None
            
#             # move on to the right side of the tree
#             node = node.right
        
        
       