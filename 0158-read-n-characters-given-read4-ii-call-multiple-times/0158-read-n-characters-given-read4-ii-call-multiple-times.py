# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.q = deque()
        
        
    def read(self, buf: List[str], n: int) -> int:
        buf4 = ["" for i in range(4)]
        while len(self.q)<n:
            count_buff = read4(buf4)
            if count_buff == 0:
                break
            for i in range(count_buff):
                self.q.append(buf4[i])
                i+=1
            buf4 = ["" for i in range(4)]
        
        i=0
        while self.q and i<n:
            ch = self.q.popleft()
            buf[i] = ch
            i+=1
        return i
            
        
        

            
        