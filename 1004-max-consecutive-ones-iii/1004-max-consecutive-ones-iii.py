from collections import deque
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        dq = deque()
        zeros = 0
        ans = 0
        for i in range(len(nums)):
            dq.append(nums[i])
            if not nums[i]:
                zeros+=1
                
            while zeros>k and dq:
                element = dq.popleft()
                if element==0:
                    zeros-=1
            ans = max(ans, len(dq))
        return ans