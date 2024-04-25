class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums)==1:
            return 0
        
        farthest = nums[0]
        next_farthest = nums[0]
        jump = 1
        
        for i in range(1, len(nums)):
            if farthest >= len(nums)-1:  
                return jump
            next_farthest = max(next_farthest, i+nums[i])
            if i == farthest:
                farthest = next_farthest
                jump+=1
            
            
            
            
            
                
            
        