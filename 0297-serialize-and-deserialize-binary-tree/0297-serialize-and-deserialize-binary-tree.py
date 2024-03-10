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
        result = ""
        if not root:
            return ""
        dq= deque()
        dq.append(root)
        while dq:
            node = dq.popleft()
            if node:
                result+=str(node.val)+","
                dq.append(node.left)
                dq.append(node.right)
            else:
                result+="None,"
        return result
            
            
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        if not data:
            return None
        node_list = data[:len(data)].split(",")
        
        dq = deque()
        root = TreeNode(node_list[0])
        dq.append(root)
        
        i = 1
        while dq and i<len(node_list):
            node = dq.popleft()
            if node_list[i] != "None":
                node.left = TreeNode(node_list[i])
                dq.append(node.left)
            i+=1
            if i<len(node_list) and node_list[i] != "None":
                node.right = TreeNode(node_list[i])
                dq.append(node.right)
            i+=1
        return root
            
            
                
            
            
            
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))