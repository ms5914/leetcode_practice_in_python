"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        count = 0
        buff4=[''] * 4
        ind = 0
        while count<n:
            t = read4(buff4)
            if t == 0:
                break
            count+=t
            i = 0
            for ch in buff4:
                buf[ind] = buff4[i]
                i+=1
                ind+=1
                
        
        end_index = min(n, count)
        buf = buf[:end_index]
        return  min(n, count)
            
            
            
        