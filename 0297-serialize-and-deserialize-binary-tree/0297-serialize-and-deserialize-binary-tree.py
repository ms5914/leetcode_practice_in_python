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
        result = []
        if not root:
            return ""
        q = deque()
        q.append(root)
        while q:
            root = q.popleft()
            if not root:
                result.append("None")
            else:
                result.append(str(root.val))
                q.append(root.left)
                q.append(root.right)
        
        return ",".join(result)
    
                
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        values = data.split(",")
        if not values or not data:
            return None
        root = TreeNode(int(values[0]))
        q = deque()
        q.append(root)
        
        i = 1
        while q:
            node = q.popleft()
            if i<len(values) and values[i] != "None":
                node.left = TreeNode(int(values[i]))
                q.append(node.left)
            else:
                node.left = None
            i+=1
            
            if i<len(values) and values[i] != "None":
                node.right = TreeNode(int(values[i]))
                q.append(node.right)
            else:
                node.right = None
            i+=1
        return root
            
            
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))