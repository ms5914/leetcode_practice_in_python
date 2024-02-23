class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        max_count = 0
        mapp = defaultdict(int)
        count = 0
        
        
        for start, end in intervals:
            mapp[start]+=1
            mapp[end]-=1
        
        for key in sorted(mapp.keys()):
            count+=mapp[key]
            
            max_count = max(max_count, count)
        
        return max_count
            
            
            
            
            
        