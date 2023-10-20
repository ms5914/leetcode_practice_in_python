class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = dict()
        counts = collections.Counter(nums)
        return True if any(val>=2 for val in counts.values()) else False
        
        