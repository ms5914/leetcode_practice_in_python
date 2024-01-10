# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append((root, 0))
        max_len = 0
        while q:
            max_len = max(q[len(q)-1][1]-q[0][1], max_len)
            q_len = len(q)
            for i in range(q_len):
                elem, ind = q.popleft()
                if elem.left:
                    q.append((elem.left, 2*ind+1))
                if elem.right:
                    q.append((elem.right, 2*ind+2))
                
        
        return max_len+1
                    
                
            
            
        