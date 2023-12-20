# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findLCA(root, p, q):
            if not root:
                return None
            if root.val == p.val or root.val == q.val:
                return root
            left = findLCA(root.left, p, q)
            right = findLCA(root.right, p, q)
            if left and right:
                return root
            return left or right   
        res = findLCA(root, p, q)
        return res
    
        