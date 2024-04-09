# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = []
        if not root:
            return 0
    
        def find_numbers_dfs(root, partial_list):
            if not root.left and not root.right:
                result.append("".join(list(partial_list)+[str(root.val)]))
            else:
                if root.left:
                    find_numbers_dfs(root.left, partial_list+[str(root.val)])
                if root.right:
                    find_numbers_dfs(root.right, partial_list+[str(root.val)])
        find_numbers_dfs(root, [])
        return sum([ int(st) for st in result if st!=""])
        