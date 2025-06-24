class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        low = 0
        high = len(nums)-1

        while low<=high:
            
            mid = (low+high)//2
            #print(low, high, mid)
            next_num = nums[mid+1] if mid+1 < len(nums) else -1*float("inf")
            prev_num = nums[mid-1] if mid-1>=0 else -1*float("inf")
            #print(prev_num, nums[mid], next_num)
            if nums[mid]>prev_num and nums[mid]>next_num:
                return mid
            elif nums[mid] < prev_num:
                high = mid-1
            else:
                low = mid+1
            
            
        