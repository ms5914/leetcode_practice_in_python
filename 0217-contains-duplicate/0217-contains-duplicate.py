class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        #Method 1
        # counts = dict()
        # counts = collections.Counter(nums)
        # return any(val>=2 for val in counts.values()) 
    
        #Method 2 - Use soritng
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i + 1]:
                return True
        return False;
    
        #Method 3 - One liner python wizardry
        return len(set(nums)) < len(nums)

        
        