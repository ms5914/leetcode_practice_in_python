class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        nums = [[k,v] for k,v in freq_map.items()]
        n = len(nums)
        K = n-k
        
        
        def quick_select(nums, p, r):
            if p==r:
                return
            partition_index = partition(nums, p, r)
            if partition_index == K:
                return
            elif partition_index < K:
                quick_select(nums, partition_index+1, r )
            else:
                quick_select(nums, p, partition_index-1 )
                
            
        
        def partition(nums, p, r):
            ind = random.randint(p,r)
            nums[ind], nums[r] = nums[r], nums[ind]
            
            start,i = p,p
            
            while i<r:
                if nums[i][1]<nums[r][1]:
                    nums[start], nums[i] = nums[i], nums[start]
                    start+=1
                i+=1
            nums[start], nums[r] = nums[r], nums[start]
            return start
        
        quick_select(nums, 0, len(nums)-1)
        
        return [num[0] for num in nums[n-k:]]
            
            
            
        