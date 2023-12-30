# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check_balanced(root):
            if not root:
                return True, 0
            else:
                is_valid_left, lheight = check_balanced(root.left)
                is_valid_right, rheight = check_balanced(root.right)
                if not is_valid_left or not is_valid_right or abs(lheight-rheight)>1:
                    return False, max(lheight, rheight)+1
                else:
                    return True, max(lheight, rheight)+1
        
        return check_balanced(root)[0]
                    