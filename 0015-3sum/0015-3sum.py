class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the array 
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            if i>0 and nums[i-1] == nums[i]:
                continue
            else:
                self.two_sum(nums,nums[i],i+1,len(nums)-1, res)
        
        return res
        
    def two_sum(self, nums, target, start, end, res):
        while start<end:
            if nums[start]+nums[end] < -1*target:
                start+=1
                while nums[start] == nums[start-1] and start<end:
                    start+=1
            elif nums[start]+nums[end] > -1*target:
                end-=1
                while nums[end] == nums[end+1] and start<end:
                    end-=1
            else:
                res.append([nums[start], nums[end], target])
                start+=1
                end-=1
                while nums[start] == nums[start-1] and start<end:
                    start+=1
                while nums[end] == nums[end+1] and start<end:
                    end-=1
                    
        


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         nums.sort()
#         for i in range(len(nums)):
#             if nums[i] > 0:
#                 break
#             if i == 0 or nums[i - 1] != nums[i]:
#                 self.twoSumII(nums, i, res)
#         return res

#     def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
#         lo, hi = i + 1, len(nums) - 1
#         while (lo < hi):
#             sum = nums[i] + nums[lo] + nums[hi]
#             if sum < 0:
#                 lo += 1
#             elif sum > 0:
#                 hi -= 1
#             else:
#                 res.append([nums[i], nums[lo], nums[hi]])
#                 lo += 1
#                 hi -= 1
#                 while lo < hi and nums[lo] == nums[lo - 1]:
#                     lo += 1


            




        