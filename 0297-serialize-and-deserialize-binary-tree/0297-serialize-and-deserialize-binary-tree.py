# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        if not root:
            return ""
        li = []
        def dfs(node):
            if not node:
                li.append("None")
                return
            li.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return "#".join(li)
    
            
        
#         Solution 1: Using queue
#         if not root:
#             return ""
#         q = deque()
#         q.append(root)
#         encoded = []
#         while q:
#             node = q.popleft()
#             if not node:
#                 encoded.append("None")
#             else:
#                 encoded.append(str(node.val))
#                 q.append(node.left)
#                 q.append(node.right)
        
#         print(encoded)
        
#         return "#".join(encoded)
                
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if not data:
            return []
        
        li = data.split("#")
        ind = 0
        def dfs():
            nonlocal ind
            if li[ind] == "None":
                return None
            root = TreeNode(li[ind])
            ind+=1
            root.left = dfs()
            ind+=1
            root.right = dfs()
            return root
        res = dfs()
        return res
            
        
        
#       Solution 1: Using queue
#         if not data:
#             return None
#         data = data.split("#")
#         print(data)
#         if not data:
#             return None
#         else:
#             q = deque()
#             index = 0
#             root = TreeNode(data[index])
#             q.append(root)
#             while q:
#                 node = q.popleft()
#                 if data[index+1] == "None":
#                     node.left = None
#                 else:
#                     node.left = TreeNode(data[index+1])
#                     q.append(node.left)
                
#                 if data[index+2] == "None":
#                     node.right = None
#                 else:
#                     node.right = TreeNode(data[index+2])
#                     q.append(node.right)
#                 index+=2
            
#             return root
                
                    
                    
                
                
                
                
                
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))