# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        if not root:
            return []
        
        q = deque()
        q.append(root)
        result= []
        ltr = True
        while q:
            q_len = len(q)
            row = []
            
            for i in range(q_len):
                node = q.popleft()
                row.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            if ltr:
                ltr = False
                result.append(row)
            else:
                ltr = True
                result.append(row[::-1])
        
        return result
                    
                
            
            
            
        
        
        