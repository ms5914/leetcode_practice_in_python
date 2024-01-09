# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        
        if not root:
            return []
        
        def find_paths(candidate, root, candidate_sum):
            if not root.left and not root.right:
                if candidate_sum == targetSum:
                    copy_list = list(candidate)
                    result.append(copy_list)
                return
            for node in [root.left, root.right]:
                if node:
                    candidate_sum+=node.val
                    candidate.append(node.val)
                    find_paths(candidate, node, candidate_sum)
                    candidate_sum-=node.val
                    candidate.pop()
        
        find_paths([root.val], root, root.val)
        return result
        
                
                