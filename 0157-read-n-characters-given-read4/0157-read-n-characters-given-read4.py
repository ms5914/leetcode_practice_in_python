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
        
        ind = 0
        
        #Question doesn't make it clear but buffer is cyclical, so you need to keep track of how many chars you need to read and copy
        buff4 = ['']*4
        while count<n:
            t = read4(buff4)
            if t == 0:
                break
            for i in range(t):
                buf[ind] = buff4[i]
                count+=1
                ind+=1
                if count == n:
                    break
        return count
            
            
            
        