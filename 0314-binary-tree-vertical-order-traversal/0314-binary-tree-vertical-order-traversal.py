# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        
        queue = deque()
        queue.append((root, 0))
        cols = defaultdict(list)
        cols[0].append(root.val)
        min_index = 0
        max_index = 0
        while queue:
            node, i = queue.popleft()
            if node.left:
                min_index = min(min_index, i-1)
                cols[i-1].append(node.left.val)
                queue.append((node.left, i-1))
            if node.right:
                max_index = max(max_index, i+1)
                cols[i+1].append(node.right.val)
                queue.append((node.right, i+1))
        for i in range(min_index, max_index+1):
            result.append(cols[i])
        return result
            
                
                
                