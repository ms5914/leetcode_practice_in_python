class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        for right in range(len(nums)):
            # If we included a zero in the window we reduce the value of k.
            # Since k is the maximum zeros allowed in a window.
            k -= 1 - nums[right]
            # A negative k denotes we have consumed all allowed flips and window has
            # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
            while k < 0 and left<=right:
                # If the left element to be thrown out is zero we increase k.
                k += 1 - nums[left]
                left += 1
            ans = max(ans, right-left+1)
            
        return ans