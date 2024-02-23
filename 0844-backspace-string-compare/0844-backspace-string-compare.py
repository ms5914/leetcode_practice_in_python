class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = s[::-1]
        t = t[::-1]
        
        def helper(s, i):
            skips_i = 0
            while i<len(s):
                if s[i] == '#':
                    skips_i = skips_i+1
                    i=i+1
                else:
                    if skips_i:
                        i = i+1
                        skips_i = skips_i-1
                    else:
                        return i
            return i
                
        
        i1, i2 = 0,0
        while i1<len(s) and i2<len(t):
            i1,i2 = helper(s,i1), helper(t,i2)
            if i1<len(s) and i2<len(t):
                if s[i1] == t[i2]:
                    i1,i2 = i1+1,i2+1
                else:
                    return False
        if i1<len(s):
            i1 = helper(s,i1)
        
        if i2<len(t):
            i2 = helper(t,i2)
    
        return i1==len(s) and i2==len(t)
        
        
        
        
        
        
        
        
        
        
        
        
#         i,j = len(s)-1, len(t)-1
#         while i>=0 and j>=0:
#             spaces = 0
#             while i>=0:
#                 if s[i] == '#':
#                     spaces+=1
#                     i-=1
#                 else:
#                     if spaces:
#                         spaces-=1
#                         i-=1
#                     else:
#                         break
           
#             spacet = 0
#             while j>=0:
#                 if t[j] == '#':
#                     spacet+=1
#                     j-=1
#                 else:
#                     if spacet:
#                         spacet-=1
#                         j-=1
#                     else:
#                         break
#             print(i,j)
            
#             if i>=0 and j>=0:
#                 if s[i] != t[j]:
#                     return False
            
#             if (i>=0 and  not j>=0) or (j>=0 and  not i>=0)  :
#                 return False
            
#             i-=1
#             j-=1
        
#         if i<0 and j<0:
#             return True
#         else:
#             return False
            
                        
            
        