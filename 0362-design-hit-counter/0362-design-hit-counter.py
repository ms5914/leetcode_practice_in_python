class HitCounter:
    
    #Approach 2: The correct approach is to maintain a queue. We keep on adding (time, freq) pairs to the queue. Now when gethit is called, we start deleting for the rear of the rear of the queue all the (timestamp, freq) pairs where time<=current_timestamp-300. Then the remaining queue size is our answer.

    def __init__(self):
        self.q = deque()
        

    def hit(self, timestamp: int) -> None:
        self.q.append((timestamp, 1))
        

    def getHits(self, timestamp: int) -> int:
        while self.q and self.q[0][0]<=timestamp-300:
            self.q.popleft()
        return(len(self.q))
            
            
        
        
    
    #Approach 1: I used 2 stacks to store (time, freq) pairs. While popping I had to add the popped elements back.
#     def __init__(self):
#         self.stack = []
#         self.stack1=[]
        
#     def hit(self, timestamp: int) -> None:
#         if not self.stack or self.stack[-1] != timestamp:
#             self.stack.append((timestamp, 1))
#         elif self.stack[-1][0] == timestamp:
#             _,freq = self.stack.pop()
#             self.stack.append((timestamp, freq+1))
        
#     def getHits(self, timestamp: int) -> int:
#         result = 0
#         if not self.stack:
#             return result
        
#         while self.stack and self.stack[-1][0]<=timestamp and self.stack[-1][0]>timestamp-300:
#             elem,freq = self.stack.pop()
#             self.stack1.append((elem,freq))
#             result+=freq
        
#         while self.stack1:
#             self.stack.append(self.stack1.pop())
#         return result
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)