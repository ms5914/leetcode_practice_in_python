import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        k_closest_heap = []
        result = []
        def find_distance(c):
            x, y = c[0], c[1]
            return math.sqrt(pow(x,2)+pow(y,2))
        
        for point in points:
            heapq.heappush(k_closest_heap, (-1*find_distance(point), point))
            if len(k_closest_heap)>k:
                heapq.heappop(k_closest_heap)
        
        while k_closest_heap:
            _, point = heapq.heappop(k_closest_heap)
            result.append(point)
        
        return result
                
        
        
        
            
        
        
        
        
            
        