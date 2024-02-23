class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
 # Solution2 Using MinHeap 
        heap = []
        intervals.sort(key=lambda v: (v[0],v[1]))
        result = 0
        for start,end in intervals:
            if not heap:
                heapq.heappush(heap, end)
            else:
                while heap and heap[0]<=start:
                    _ = heapq.heappop(heap)
                heapq.heappush(heap, end)
            result = max(result, len(heap))
        return result
 # Solution 1: Line Sweep (Easier and better)
#         max_count = 0
#         mapp = defaultdict(int)
#         count = 0
#         for start, end in intervals:
#             mapp[start]+=1
#             mapp[end]-=1
        
#         for key in sorted(mapp.keys()):
#             count+=mapp[key]
#             max_count = max(max_count, count)
        
#         return max_count


            
            
            
            
            
        