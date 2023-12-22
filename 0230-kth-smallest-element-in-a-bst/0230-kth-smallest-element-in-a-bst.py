# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = -1
        target = k-1
        elem = -1
        
        def findksmallest(root):
            nonlocal elem
            nonlocal count
            if not root:
                return 
            findksmallest(root.left)
            count+=1
            if count == target:
                elem = root.val
            findksmallest(root.right)
        
        findksmallest(root)
        return elem
            
            
            
        