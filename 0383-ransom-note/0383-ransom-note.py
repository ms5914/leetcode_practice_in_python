class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn = ''.join(sorted(ransomNote))
        m = ''.join(sorted(magazine))
        i,j = 0,0
        while i<len(rn) and j<len(m):
            if rn[i] == m[j]:
                i+=1
                j+=1
            elif ord(rn[i]) < ord(m[j]):
                return False
            else:
                j+=1
        if i==len(rn):
            return True
        return False
        
        