class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 0
        for i in range(0, len(nums)-2):
            low = i+1
            high = len(nums)-1
            new_target = target-nums[i]
            while low<high:
                if nums[low]+nums[high]<new_target:
                    result+=(high-low)
                    low+=1
                else:
                    high-=1
        
        return result
                    
                    
                
                