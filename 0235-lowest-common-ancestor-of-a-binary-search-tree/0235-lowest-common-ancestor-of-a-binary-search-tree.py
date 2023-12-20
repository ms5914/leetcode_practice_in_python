# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        #This solution works also if the given tree is not a BST.
        def findLCA(root, p, q):
            #If we are at a leaf node and we couldn't find either value
            if not root:
                return None
            
            #If we found one value, that means there is a possibility that this is the lca, the parent call will decide
            if root.val == p.val or root.val == q.val:
                return root
            left = findLCA(root.left, p, q)
            right = findLCA(root.right, p, q)
            
            #If one value is in left and other is on the right then this is the LCA
            if left and right:
                return root
            return left or right   
        
        #This one uses the ordering present in a BST
        def findLCA_bst(root, p, q):
            if not root:
                return None
            if p.val<root.val and q.val<root.val:
                return findLCA_bst(root.left, p, q)
            elif p.val>root.val and q.val>root.val:
                return findLCA_bst(root.right, p, q)
            else:
                return root
            
        
        
        res = findLCA_bst(root, p, q)
        return res
    
        