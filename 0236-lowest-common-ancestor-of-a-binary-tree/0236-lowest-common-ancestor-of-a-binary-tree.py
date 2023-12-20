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
            if root.val in (p.val, q.val):
                return root
            else:
                left = findLCA(root.left, p, q)
                right = findLCA(root.right, p, q)
                if left and right:
                    return root
                else:
                    return left or right
                
        return findLCA(root, p, q)
        
        
    
        