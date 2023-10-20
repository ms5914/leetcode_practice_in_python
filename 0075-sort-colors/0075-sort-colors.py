class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Dutch national flag problem - solved using two pointers
        #zero_tracker on left, two_tracker on the right
        
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
                
#Remember this tricky part: you can see that the numbers before i index is always 0 or 1, so when we meet a 0 we only need to swap 0 to the left once and increase i. But when we meet a 2, after swapping, the current number at index i is 0/1/2, we still need to handle it.
        
                
                
                
        
        