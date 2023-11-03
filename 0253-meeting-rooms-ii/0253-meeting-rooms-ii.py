class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_times = [interval[0] for interval in intervals]
        start_times.sort()
        end_times = [interval[1] for interval in intervals]
        end_times.sort()

        count = 0
        res_count = 0
         
        i,j = 0, 0

        while i<len(start_times) and j<len(end_times):
            if start_times[i]<end_times[j]:
                count+=1
                i+=1
            else: 
                count-=1
                j+=1
            res_count=max(res_count, count)
        
        return res_count

        