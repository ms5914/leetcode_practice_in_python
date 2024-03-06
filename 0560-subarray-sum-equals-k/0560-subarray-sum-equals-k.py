class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = defaultdict(int)
        hm[0] = 1

        count = 0
        cumm_sum = 0
        for i,n in enumerate(nums):
            cumm_sum+=n
            if cumm_sum-k in hm:
                count+=hm[cumm_sum-k]
            hm[cumm_sum]+=1 
        return count 
                
        