# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        column_values = defaultdict(list)
        min_col = float('inf')
        max_col = -float('inf')
        
        def dfs(node,row,column_no):
            nonlocal min_col, max_col 
            
            if not node: 
                return 
            min_col = min(min_col, column_no)
            max_col = max(max_col, column_no)
            column_values[column_no].append((row,node.val))
            dfs(node.left,row+1, column_no-1)
            dfs(node.right, row+1, column_no+1)
        
        dfs(root, 0, 0)
        
        result = []
        for col in range(min_col, max_col+1):
            li = list(sorted(column_values[col]))
            result.append([element[1] for element in li])

        return result
            
            
            
            
        