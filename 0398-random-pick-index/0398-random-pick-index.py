import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.mapp = defaultdict(list)
        for index,num in enumerate(self.nums):
            self.mapp[num].append(index)
        
    def pick(self, target: int) -> int:
        index_list = self.mapp[target]
        return index_list[random.randint(0, len(index_list)-1)]
        
        
        
        #Approach 2: Reservoir sampling : See discuss for more explaination
# https://www.youtube.com/watch?v=A1iwzSew5QY&pp=ygUScmVzZXJ2b2lyIHNhbXBsaW5n


#         count = 0
#         result = -1
#         for index,num in enumerate(self.nums):
#             if target == num:
#                 count+=1
#                 r_num = random.randint(0, count-1)
#                 if r_num == 0:
#                     result = index
                
#         return result
                
                
                
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)