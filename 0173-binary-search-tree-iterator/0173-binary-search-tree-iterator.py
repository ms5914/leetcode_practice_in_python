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
        
#Solution 2: Emulate inorder using stack. The next element should always be on the top of the stack. After popping add the left most child of the right child of the popped element.
# public class BSTIterator {

#     private TreeNode visit;
#     private Stack<TreeNode> stack;
    
#     public BSTIterator(TreeNode root) {
#         visit = root;
#         stack = new Stack();
#     }

#     public boolean hasNext() {
#         return visit != null || !stack.empty();
#     }

#     public int next() {
#         while (visit != null) {
#             stack.push(visit);
#             visit = visit.left;
#         }
#         TreeNode next = stack.pop();
#         visit = next.right;
#         return next.val;
#     }
# }




# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()