import heapq
class Solution(object):
    
    #Method 3 : Using heap and sorting
    #heap based solution 
   # https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/2002347/Very-Clearly-Explained-Heap-Solution-in-Python-Easy-to-Understand!!!
    def jobScheduling(self, startTime, endTime, profit):
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(key = lambda x:x[0])
        heap = []
        for job in jobs:
            heap.append((job[1], job[2]))

        heapq.heapify(heap)
        maxProfit = 0
        for job in jobs:
            while heap and job[0] >= heap[0][0]:
                maxProfit = max(maxProfit, heapq.heappop(heap)[1])
            heapq.heappush(heap, (job[1], job[2]+maxProfit))

        maxProfit = 0
        while heap:
            maxProfit = max(maxProfit, heapq.heappop(heap)[1])

        return maxProfit
        
        
            
            
            
            
        
        
    
    
    
    # Method 2: DP dervied from recursion with memoization
#     def jobScheduling(self, startTime, endTime, profit):
#         """
#         :type startTime: List[int]
#         :type endTime: List[int]
#         :type profit: List[int]
#         :rtype: int
#         """
#         n = len(profit)
#         self.maxsize = n
#         jobs = []

#         for i in range(n):
#             jobs.append((startTime[i], endTime[i], profit[i]))
#         jobs.sort(key = lambda x: x[0])
#         self.jobs = jobs

#         max_profit = self.find_max_profit()
#         return max_profit

    
#     def find_max_profit(self):
#         profit = [0] * len(self.jobs) 
#         profit[len(self.jobs)-1] = self.jobs[len(self.jobs)-1][2]
        
#         for i in range(len(self.jobs)-2, -1, -1):
#             j = bisect.bisect_left(self.jobs, self.jobs[i][1], key=lambda x:x[0])
            
#             if j==len(self.jobs):
#                 profit[i] = max(self.jobs[i][2], profit[i+1])
#             else:
#                 profit[i] = max(self.jobs[i][2]+profit[j], profit[i+1])
#         return profit[0]
    
    #     Method 1 : Using memoization with recursion
#     def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
#         n = len(profit)
#         self.maxsize = n
#         jobs = []

#         for i in range(n):
#             jobs.append((startTime[i], endTime[i], profit[i]))
#         jobs.sort(key = lambda x: x[0])
#         self.jobs = jobs

#         max_profit = self.find_max_profit(0, n)
#         return max_profit

    # @lru_cache(maxsize=None)
    # def find_max_profit(self, current, n):
    #     if current == n:
    #         return 0
    #     current_end_time = self.jobs[current][1]
    #     next_index = bisect.bisect_left(self.jobs, current_end_time, key = lambda x: x[0])
    #     if next_index==0:
    #         next_index = next_index+1
    #     max_profit= max(self.jobs[current][2]+self.find_max_profit(next_index,n), self.find_max_profit(current+1,n))
    #     return max_profit
    
    



