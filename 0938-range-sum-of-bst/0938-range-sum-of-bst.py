# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        result = 0
        def find_sum(root):
            print(root.val)
            if not root:
                return
            nonlocal result
            if low<=root.val<=high:
                result+=root.val
            
            if root.left and low < root.val:
                find_sum(root.left)
            if root.right and root.val <high:
                find_sum(root.right)
        
        find_sum(root)
        return result
        
                
            
        