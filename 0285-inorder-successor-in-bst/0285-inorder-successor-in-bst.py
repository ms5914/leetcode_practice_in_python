# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        result_node = None
        found=False
        prev = None
        def in_order(root):
            nonlocal result_node
            nonlocal found
            nonlocal prev
            if found:
                return
            if root is not None:
                in_order(root.left)
                if prev is not None and prev.val == p.val and not found: #you forgot "and not found" here. Because this part may still execute even if you have found the node in left subtree and then it will again use the same prev / the other alternative is to update the prev even if you have found the desired prev
                    result_node = root
                    found = True
                    #prev = root This is required if you are not using " and not found"
                    return
                prev = root
                in_order(root.right)
        
        in_order(root)
        
        if found and result_node:
            return result_node
        else:
            return None

        
        
        
                
                
                
                
            
        