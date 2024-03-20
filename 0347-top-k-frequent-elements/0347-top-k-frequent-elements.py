class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #Can be done using heaps / Quick select and the easiest one and most efficient is using bucket sort. 
        
        bucket = [[] for _ in range(len(nums) + 1)]
        Count = Counter(nums).items()  
        for num, freq in Count: bucket[freq].append(num) 
        flat_list = [item for sublist in bucket for item in sublist]
        return flat_list[::-1][:k]
        
        