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
        
        def setNodes(start, end):
            if not nums or end>=len(nums) or start<0 or end<start:
                return None
            mid = start+(end-start)//2
            root = TreeNode(val=nums[mid])
            root.left = setNodes(start, mid-1)
            root.right = setNodes(mid+1, end)
            return root
        
        return setNodes(0, len(nums)-1)
        