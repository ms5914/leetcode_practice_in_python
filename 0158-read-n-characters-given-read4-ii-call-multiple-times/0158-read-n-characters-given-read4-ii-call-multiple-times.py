# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.buff_internal = [0 for i in range(4)]
        self.i1, self.n1 = 0,0
        
    def read(self, buf: List[str], n: int) -> int:
        i = 0
        while i<n:
            if self.i1 >= self.n1:
                self.i1 = 0
                self.n1 = read4(self.buff_internal)
                if self.n1 == 0:
                    break
            buf[i] = self.buff_internal[self.i1]
            i+=1
            self.i1+=1
        return i
                
        
        
    #     public int read(char[] buf, int n) {      // this question is about internal buffer and external buffer
    # // internal buffer: i4, n4, buf4
    # // external buffer: i, n, buf
    #     int i = 0;
    #     while (i < n) {     // external buf limitation
    #         if (i4 >= n4) {     // internal buf limitation
    #             i4 = 0;
    #             n4 = read4(buf4);
    #             if (n4 == 0) break;
    #         }
    #         buf[i++] = buf4[i4++];
    #     }
    #     return i;
    # }
    # char[] buf4 = new char[4];
    # int i4 = 0, n4 = 0;