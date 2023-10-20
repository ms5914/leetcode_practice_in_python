class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        result = []
        result.append(intervals[0])
        
        for i in range(1, len(intervals)):
            
            if not intervals[i][0] > result[-1][1]:
                top_interval = result.pop()
                result.append([min(intervals[i][0], top_interval[0]), max(intervals[i][1], top_interval[1]) ])
            else:
                result.append(intervals[i])
        
        return result
                
        