import bisect
class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.hm[key]
        if not values:
            return ""
        else:
            index = bisect.bisect_left(values,timestamp, key=lambda x: x[0])
            if index == len(values):
                return values[index-1][1]
            elif index == 0 and values[index][0]!=timestamp:
                return ""
            elif values[index][0] == timestamp:
                return values[index][1]
            else:
                return values[index-1][1]
    
            
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)