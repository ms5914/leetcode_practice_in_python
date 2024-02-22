import heapq

class FreqStack:

    def __init__(self):
        self.freq_map = {} #To track latest freq of an element (after pushes and pops and then accordingly add to heap)
        self.heap = []  #This heap has (freq, time, elem). There are multiple entries of the same element in this heap. Freq and time is how we decide what to pop. 
        self.t = 0   #To track which elem is closest to the top kinda like time of push
        
    
    def push(self, val: int) -> None:
        
        if val in self.freq_map:
            self.freq_map[val]+=1
        else:
            self.freq_map[val] = 1 
            
        
        self.t +=1
        heapq.heappush(self.heap, (-self.freq_map[val], -self.t, val))    
        

    def pop(self) -> int:
        _, _, val = heapq.heappop(self.heap)
        self.freq_map[val]-=1
        return val
        
        
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()






