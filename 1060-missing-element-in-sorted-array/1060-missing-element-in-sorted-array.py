class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        end = len(nums)-1
        start = 0
        
        while start<end:
            # print(start, end, k)
            mid = end-(end-start)//2
            missing = nums[mid] - (nums[start]+(mid-start))
            if  missing < k:
                start = mid
                k = k-missing
            else:
                end = mid-1
        
        return nums[start]+k
        