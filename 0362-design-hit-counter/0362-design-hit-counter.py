class HitCounter:

    def __init__(self):
        self.stack = []
        self.stack1=[]
        
    def hit(self, timestamp: int) -> None:
        if not self.stack or self.stack[-1] != timestamp:
            self.stack.append((timestamp, 1))
        elif self.stack[-1][0] == timestamp:
            _,freq = self.stack.pop()
            self.stack.append((timestamp, freq+1))
        
    def getHits(self, timestamp: int) -> int:
        result = 0
        if not self.stack:
            return result
        
        while self.stack and self.stack[-1][0]<=timestamp and self.stack[-1][0]>timestamp-300:
            elem,freq = self.stack.pop()
            self.stack1.append((elem,freq))
            result+=freq
        
        while self.stack1:
            self.stack.append(self.stack1.pop())
        return result


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)