class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        new_interval = newInterval
        added = False
        for interval in intervals:
            if interval[1]<new_interval[0]:
                result.append(interval)
            elif interval[0]>new_interval[1]:
                if not added:
                    added = True
                    result.append(new_interval)
                result.append(interval)
            else:
                new_interval = [min(interval[0], new_interval[0]), max(interval[1], new_interval[1])]
                
            
        if not added:
            result.append(new_interval)
            
        return result
                
            
        