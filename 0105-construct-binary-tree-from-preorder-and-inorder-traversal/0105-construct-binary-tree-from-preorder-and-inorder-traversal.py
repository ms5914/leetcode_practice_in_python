# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        val_index = {val: ind for ind,val in enumerate(inorder)}
        preorder_ind = 0
        def find_tree(start, end):
            nonlocal preorder_ind
            # if preorder_ind>=len(preorder) or start>end:
            #     return None
            
            root = TreeNode(preorder[preorder_ind])
            inorder_ind = val_index[preorder[preorder_ind]]
            
            if inorder_ind>start:
                preorder_ind+=1
                root.left = find_tree(start, inorder_ind-1)
            
            if inorder_ind<end:
                preorder_ind+=1
                root.right = find_tree(inorder_ind+1, end)
            
            return root

        return find_tree(0, len(inorder)-1)
                            