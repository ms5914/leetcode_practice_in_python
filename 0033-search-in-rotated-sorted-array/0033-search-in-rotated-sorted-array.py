class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
#         low = 0
#         high = len(nums)-1
        
#         while low<=high:
#             mid = low+(high-low)//2
#             if nums[mid] == target:
#                 return mid
#             if nums[mid]<target:
#                 if nums[mid]>=nums[low] and nums[mid]>=nums[high]:
#                     low=mid+1
#                 else:
#                     if target<=nums[high]:
#                         low = mid+1
#                     else:
#                         high = mid-1
            
#             elif nums[mid]>target:
#                 if nums[mid]>=nums[low] and nums[mid]>=nums[high]:
#                     if target<nums[low]:
#                         low = mid+1
#                     else:
#                         high = mid-1
#                 else:
#                     high = mid-1
            
#         return -1
                
    #Better approach : Just figure out which side is sorted and proceed. 
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            
            # Case 1: find target
            if nums[mid] == target:
                return mid
            
            # Case 2: subarray on mid's left is sorted
            elif nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            # Case 3: subarray on mid's right is sorted.
            else:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
                
        