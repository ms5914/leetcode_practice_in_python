class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        for index, (i,j) in enumerate(zip(s,t)):
            if i == j:
                continue
            else:
                return s[index+1:] == t[index:] or s[index:] == t[index+1:] or s[index+1:] == t[index+1:]
        
        return abs(len(s)-len(t))==1
        