from functools import lru_cache
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        @lru_cache(maxsize=None)
        def is_match(start_s, start_p):
            
            if  start_p == len(p):
                return start_s == len(s)
            
            i, j = start_s,start_p
            if j<len(p)-1 and p[j+1] == "*":
                return ((i<len(s) and (s[i] == p[j] or p[j] == ".")) and is_match(i+1, j)) or is_match(i,j+2)
            else:
                return (i<len(s) and (s[i] == p[j] or p[j] == ".")) and is_match(i+1, j+1)
        
        return is_match(0,0)


                
        
        
        
        
        
        