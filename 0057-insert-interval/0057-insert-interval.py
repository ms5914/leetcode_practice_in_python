class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        result = []
        is_inserted = False
        for interval in intervals:
            if new_interval[1]<interval[0]:
                if not is_inserted:
                    is_inserted= True
                    result.append(new_interval)
                result.append(interval)
            elif interval[1]<new_interval[0]:
                result.append(interval)
            else:
                new_interval[0] = min(interval[0], new_interval[0])
                new_interval[1] = max(interval[1], new_interval[1])
            
        if not is_inserted:
            result.append(new_interval)
        
        return result