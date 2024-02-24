class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda v: (v[1],v[0]))
        heap = []
        result = 0
        for start, end in points:
            if not heap:
                result+=1
                heap.append(end)
            else:
                if start>heap[0]:
                    heap[0] = end
                    result+=1
        return result