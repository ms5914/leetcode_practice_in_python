import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        

    def addNum(self, num: int) -> None:
        max_heap_len = len(self.max_heap)
        min_heap_len = len(self.min_heap)
        if max_heap_len == min_heap_len:
            heapq.heappush(self.max_heap, -1*heapq.heappushpop(self.min_heap, num))
        else:
            heapq.heappush(self.min_heap, -1*heapq.heappushpop(self.max_heap, -1*num))
            
            
            
        
#         if not self.max_heap and not self.min_heap:
#             heapq.heappush(self.max_heap, -1*num)
#         else:
#             if num < -1*self.max_heap[0]:
#                 heapq.heappush(self.max_heap, -1*num)
#             else:
#                 heapq.heappush(self.min_heap, num)
                
#         while abs(len(self.max_heap)-len(self.min_heap))>1:
#             if len(self.max_heap) > len(self.min_heap):
#                 heapq.heappush(self.min_heap, -1*heapq.heappop(self.max_heap))
#             else:
#                 heapq.heappush(self.max_heap, -1*heapq.heappop(self.min_heap))
            
    
    def findMedian(self) -> float:
        max_heap_len = len(self.max_heap)
        min_heap_len = len(self.min_heap)
        if min_heap_len == max_heap_len:
            return (-1*self.max_heap[0]+self.min_heap[0])/2
        else:
            return -1*self.max_heap[0]
    
    
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()