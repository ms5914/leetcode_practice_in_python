# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        result = -float("inf")
        
        def find_sum(node):
            nonlocal result
            left_sum, right_sum = 0,0
            if node.left:
                left_sum = max(0,find_sum(node.left))
            if node.right:
                right_sum = max(0,find_sum(node.right))
            
            result = max(result, node.val+left_sum+right_sum)
            
            return node.val+max(left_sum,right_sum)
        
        find_sum(root)
        return result
            
            
            
            
            
                
                
            
            
                
        