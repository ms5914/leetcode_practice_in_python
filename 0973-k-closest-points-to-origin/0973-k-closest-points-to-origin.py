import math
import heapq
import random
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        
        
        #Approach 2: Quick select
            
        def find_distance_from_origin(coord):
            x, y = coord[0], coord[1]
            return math.sqrt(pow(x,2)+pow(y,2))
        
            
       
        dist_coord_list = []
        for coord in points:
            dist_coord_list.append((find_distance_from_origin(coord), coord))
            
        
        
        def quick_sort(A, p,r,k):
            
            #Remember the equal sign
            if p<=r:
                q = partition(A, p,r)
                if q == k-1:
                    return [pair for dist, pair in A[:q+1]]
                elif q<k-1:
                    return quick_sort(A, q+1, r,k)
                else:
                    return quick_sort(A,p,q-1,k)
            
                
                
            
        def partition(A, p, r):
            rand_index = random.randint(p,r)
            
            #You forgot doing this 
            A[rand_index], A[r] = A[r], A[rand_index]
        
            start, i = p,p
            end = r
            while i<=end:
                if A[i][0]<A[r][0]:
                    A[start], A[i] = A[i], A[start]
                    start+=1
                    i+=1
                else:
                    i+=1
            A[start], A[r] = A[r], A[start]
            return start
        
        return quick_sort(dist_coord_list, 0, len(dist_coord_list)-1, k)
            
            
            
            
            
            
            
            
            
            
        
        #Approach1: Heap
#         k_closest_heap = []
#         result = []
#         def find_distance(c):
#             x, y = c[0], c[1]
#             return math.sqrt(pow(x,2)+pow(y,2))
        
#         for point in points:
#             heapq.heappush(k_closest_heap, (-1*find_distance(point), point))
#             if len(k_closest_heap)>k:
#                 heapq.heappop(k_closest_heap)
        
#         while k_closest_heap:
#             _, point = heapq.heappop(k_closest_heap)
#             result.append(point)
        
#         return result







                
        
        
        
            
        
        
        
        
            
        