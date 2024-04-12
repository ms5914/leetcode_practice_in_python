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
                left_sum = find_sum(node.left)
            if node.right:
                right_sum = find_sum(node.right)
            
            result = max(result,max(node.val , max(max(node.val+right_sum, node.val+left_sum), node.val+left_sum+right_sum)))
            
            return max(node.val, max(node.val+left_sum, node.val+right_sum))
        
        find_sum(root)
        return result
            
            
            
            
            
                
                
            
            
                
        