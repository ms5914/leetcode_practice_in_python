# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count_paths = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        
        running_sum = 0
        if not root:
            return 0
        def find_paths(node):
            nonlocal count_paths
            nonlocal running_sum
            running_sum+=node.val
            
            
            if running_sum-targetSum in prefix_sums:
                count_paths+=prefix_sums[running_sum-targetSum]
                
            prefix_sums[running_sum]+=1
            for child_node in (node.left, node.right):
                if child_node:
                    find_paths(child_node)
            
            prefix_sums[running_sum]-=1
            running_sum-=node.val
            
            
            
        
        find_paths(root)
        return count_paths
            
                    

            
                
     