class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Dutch national flag problem - solved using two pointers
        
        zero_tracker = i = 0
        two_tracker = len(nums)-1
        
        
        while i<=two_tracker:
            if nums[i] == 1:
                i+=1
            elif nums[i] == 0:
                nums[zero_tracker], nums[i] = nums[i], nums[zero_tracker]
                i+=1
                zero_tracker+=1
            elif nums[i] == 2:
                nums[two_tracker], nums[i] = nums[i], nums[two_tracker]
                two_tracker-=1
        
                
                
                
        
        