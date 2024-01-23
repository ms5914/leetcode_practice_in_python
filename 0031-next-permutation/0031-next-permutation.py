class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        
        def reverse(start, end):
            while start<end:
                nums[start], nums[end] = nums[end], nums[start]
                start+=1
                end-=1
            
            
        i =  len(nums)-1
        while i>0 and nums[i-1]>=nums[i]:
            i-=1
        
        if i>0:
            j = i-1
            k = i
            while k<len(nums) and nums[k]>nums[j]:
                k+=1
            nums[k-1], nums[j] = nums[j], nums[k-1]
        
        
        reverse(i, len(nums)-1)
        
        
        
        
            
            
        