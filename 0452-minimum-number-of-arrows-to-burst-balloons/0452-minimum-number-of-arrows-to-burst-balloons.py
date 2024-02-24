class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda v: (v[1],v[0]))
        prev = None
        result = 0
        for start, end in points:
            if not prev:
                result+=1
                prev = end
            else:
                if start>prev:
                    prev = end
                    result+=1
        return result
    
    
    