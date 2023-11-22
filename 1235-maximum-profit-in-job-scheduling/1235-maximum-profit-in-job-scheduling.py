import bisect
from functools import lru_cache 
class Solution:
    
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        self.maxsize = n
        jobs = []

        for i in range(n):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs.sort(key = lambda x: x[0])
        self.jobs = jobs

        max_profit = self.find_max_profit(0, n)
        return max_profit

    @lru_cache(maxsize=None)
    def find_max_profit(self, current, n):
        if current == n:
            return 0
        current_end_time = self.jobs[current][1]
        next_index = bisect.bisect_left(self.jobs, current_end_time, key = lambda x: x[0])
        if next_index==0:
            next_index = next_index+1
        max_profit= max(self.jobs[current][2]+self.find_max_profit(next_index,n), self.find_max_profit(current+1,n))
        return max_profit
    
            
            
            