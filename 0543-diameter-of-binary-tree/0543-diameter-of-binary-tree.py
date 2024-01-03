# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def find_diameter(root):
            nonlocal diameter
            
            if not root:
                return 0
            
            else:
                h_left = find_diameter(root.left)
                h_right = find_diameter(root.right)
                
                diameter = max(diameter, h_left+h_right+1)
                
                return h_left+1 if h_left>h_right else h_right+1
            
        find_diameter(root)
        
        return diameter-1
                
            
        