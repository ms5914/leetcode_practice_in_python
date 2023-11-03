class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hm = {}
        hm[0] = -1
        running_sum = 0
        max_len = 0
        for i,num in enumerate(nums):
            running_sum +=(1 if num == 1 else -1)
            if running_sum in hm:
                max_len = max(max_len, i-hm[running_sum])
            else:
                hm[running_sum] = i
        
        return max_len



# Thus, we make use of a HashMap mapmapmap to store the entries in the form of (index,count)(index, count)(index,count). We make an entry for a countcountcount in the mapmapmap whenever the countcountcount is encountered first, and later on use the correspoding index to find the length of the largest subarray with equal no. of zeros and ones when the same count is encountered again.