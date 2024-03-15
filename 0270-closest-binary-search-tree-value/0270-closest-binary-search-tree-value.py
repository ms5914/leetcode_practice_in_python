# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        result = None
        min_diff = float("inf")
        def find_closest(root):
            nonlocal result, min_diff
            if not root:
                return
            if abs(abs(root.val) -abs(target))<min_diff:
                min_diff = abs(abs(root.val) -abs(target))
                result = root.val
            if abs(abs(root.val) -abs(target)) == min_diff:
                result = min(root.val, result)
                
            if target > root.val:
                find_closest(root.right)
            if target < root.val:
                find_closest(root.left)
        find_closest(root)
        return result
    
    
    #Efficient iterative binary search:

# class Solution:
#     def closestValue(self, root: TreeNode, target: float) -> int:
#         closest = root.val
#         while root:
#             closest = min(root.val, closest, key = lambda x: (abs(target - x), x))
#             root = root.left if target < root.val else root.right
#         return closest
            
                
            
        