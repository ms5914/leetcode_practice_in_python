# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        def isValid(root, min_val, max_val):
            if not root:
                return True
            if root.val<=min_val or root.val>=max_val:
                return False
            #Remember that we will still take the old min/max value based on which side we are recursing on recursion. (min_val, max_val)
            return isValid(root.left, min_val, root.val) and isValid(root.right, root.val, max_val)
        
       
        return isValid(root.left,-1*float("inf"), root.val) and isValid(root.right, root.val, float("inf"))