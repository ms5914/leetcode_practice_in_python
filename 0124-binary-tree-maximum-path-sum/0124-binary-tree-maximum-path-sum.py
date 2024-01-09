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
        
        max_sum = -1*float("inf")
        def find_max_sum(root):
            if not root: 
                return 0
            nonlocal max_sum
            left_sum = find_max_sum(root.left)
            right_sum = find_max_sum(root.right)
            
            max_sum = max(max_sum, left_sum+right_sum+root.val, left_sum+root.val, right_sum+root.val, root.val)
            
            return max(left_sum+root.val, right_sum+root.val, root.val)
        
        find_max_sum(root)
        return max_sum
        