# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        if not nums:
            return None
        
        def setNodes(nums):
            if not nums:
                return None
            root = TreeNode(val=nums[len(nums)//2])
            root.left = setNodes(nums[0:len(nums)//2])
            root.right = setNodes(nums[len(nums)//2+1:])
            return root
        
        return setNodes(nums)
        