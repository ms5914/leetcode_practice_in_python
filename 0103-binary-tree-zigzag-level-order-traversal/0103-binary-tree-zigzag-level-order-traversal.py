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
            row = deque() #Make this as queue because now while creating a candidate row, we can either append to the left or to the right in O(1) time
            
            if ltr:
                ltr = False
                for i in range(q_len):
                    node = q.popleft()
                    row.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            else:
                ltr = True
                for i in range(q_len):
                    node = q.popleft()
                    row.appendleft(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    
            
            result.append(row)
            
        
        return result
                    
                
            
            
            
        
        
        