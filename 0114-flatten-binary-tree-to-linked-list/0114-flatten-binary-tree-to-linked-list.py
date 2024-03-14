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
        
       