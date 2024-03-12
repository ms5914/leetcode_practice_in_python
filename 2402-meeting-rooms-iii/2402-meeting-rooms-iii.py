import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x: x[0])
        
        heap_meetings = []
        heap_available = []
        room_count_dict = defaultdict(int)
        
        for i in range(n):
            heapq.heappush(heap_available, (i,0))
        
        
        i = 0
        while i<len(meetings):
            start_time = meetings[i][0]
            end_time = meetings[i][1]
            # print(f"start time: {start_time}, end_time: {end_time}")
        
            while heap_meetings and heap_meetings[0][0]<=start_time:
                room_available_time, room = heapq.heappop(heap_meetings)
                heapq.heappush(heap_available, (room,room_available_time))
            
            if not heap_available:
                room_available_time, room = heapq.heappop(heap_meetings)
                heapq.heappush(heap_available, (room,room_available_time))

            room, room_available_time  = heapq.heappop(heap_available)
            if room_available_time > start_time:
                end_time = end_time+(room_available_time-start_time)
            heapq.heappush(heap_meetings, (end_time, room))
            room_count_dict[room]+=1
            i+=1
            # print("Heap meetings", heap_meetings)
            # print("Heap available", heap_available)
            # print("room_count_dict", room_count_dict)
        
        
        max_count = -1*float("inf")
        res = 0
        for i in range(n):
            if room_count_dict[i] > max_count:
                max_count = max(max_count, room_count_dict[i])
                res = i
        return res
                
        
            
            
            
        
        
        
            
            
        
            
            
            
                
            
            
            
        