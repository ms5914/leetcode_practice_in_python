# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.head = self.curr = TreeNode(-1)
        self.inorder_traversal(root)
        
    def inorder_traversal(self, node):
        if not node:
            return
        else:
            self.inorder_traversal(node.left)
            self.curr.right = node
            self.curr = self.curr.right
            self.inorder_traversal(node.right)
            
        

    def next(self) -> int:
        self.head = self.head.right
        return self.head.val
        
        

    def hasNext(self) -> bool:
        if not self.head.right:
            return False
        return True
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()