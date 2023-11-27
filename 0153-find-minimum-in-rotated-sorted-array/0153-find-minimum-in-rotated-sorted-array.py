class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        if not nums:
            return -1
        
        while low<=high:
            mid = low+(high-low)//2
            if nums[mid]>nums[-1]:
                low = mid+1
            else:
                high = mid-1
        return nums[low]
        