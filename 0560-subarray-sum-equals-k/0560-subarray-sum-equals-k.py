class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = defaultdict(int)
        curr_sum = 0
        count = 0
        hm[0]=1 #Remember this to count subarrays that start from index 0 and has the target sum already
        for i, num in enumerate(nums):
            curr_sum+=num
            if curr_sum-k in hm:
                count+=hm[curr_sum-k]
            hm[curr_sum]+=1
        return count

