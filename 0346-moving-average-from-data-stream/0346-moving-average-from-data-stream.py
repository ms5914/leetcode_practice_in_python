class MovingAverage:

    def __init__(self, size: int):
        self.window = size
        self.dq = deque()
        self.running_sum = 0

    def next(self, val: int) -> float:
        while len(self.dq)>=self.window:
            pop_val = self.dq.popleft()
            self.running_sum-=pop_val
        self.dq.append(val)
        self.running_sum+=val
        return self.running_sum/len(self.dq)
        
        
        
        
            
            
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)