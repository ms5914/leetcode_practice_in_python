class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if len(nums) in (1,0): return 0
        
        #Approach 2: Use Hashmap to find the number of elements that are curr_num+1 or curr_num-1 
        hm = defaultdict(int)
        max_count = 0
        for num in nums:
            hm[num]+=1
            if num-1 in hm:
                max_count = max(max_count, hm[num-1]+hm[num])
            if num+1 in hm:
                max_count = max(max_count, hm[num+1]+hm[num])
        return max_count
                
                
            
            
        
        
        # Since we need to find a subsequence, order in this question won't matter. Also since we need that the  distance between max and min in subsequence should be 1. There cannot be any number in between those two in the subsequence because then the max difference won't be one
        # Approach 1 sort the array : We will then have a sequence of repeated numbers in sorted order ex. 1,1,1,4,4,4,5,5,5
        # and then for every sequence of repeated numbers, if the difference between prev repeated seq and current repeated seq is 1, update res to be the sum of both sequences else update prev_sequence_count to be the length of new_current_sequence_count and find new_current_sequence_count in next iteration
        
#         nums.sort()
#         i = 1
#         pre_count = 1
#         res = 0
#         while i<=len(nums)-1:
#             while i<=len(nums)-1 and nums[i] == nums[i-1]:
#                 pre_count+=1
#                 i+=1
            
#             if i<=len(nums)-1 and  nums[i]!=nums[i-1]:
#                 if nums[i]-nums[i-1] == 1:
#                     count = 1
#                     while i<len(nums)-1 and nums[i] == nums[i+1]:
#                         count+=1
#                         i+=1
#                     res = max(res, pre_count+count)
#                     pre_count = count
#                     i+=1
#                 else:
#                     pre_count = 1
#                     i+=1
#         return res






                        
                
            
            
            
            
        