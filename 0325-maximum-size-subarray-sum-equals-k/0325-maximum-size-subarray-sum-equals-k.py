class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        mapp = dict()
        current_sum = 0
        result = 0
        for index,value in enumerate(nums):
            current_sum+=value
            
            if current_sum==k:
                result = max(result, index+1)
                
            if current_sum-k in mapp:
                result = max(result, index-mapp[current_sum-k])         
                
            if current_sum not in mapp:
                mapp[current_sum] = index
            
            
        return result