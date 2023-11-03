class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_sum = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)):
            start, end = i+1, len(nums)-1
            while start<end:
                closest_sum = nums[i]+nums[start]+nums[end]
                if closest_sum<target:
                    start+=1
                elif closest_sum == target:
                    return closest_sum
                else:
                    end-=1
                if abs(closest_sum-target)<abs (min_sum-target):
                    min_sum = closest_sum 
        return min_sum


