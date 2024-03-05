class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        i = 0
        j = len(s)-1
        
        count = 0
        while i<=j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                count = 1
                s1 = s[i+1:j+1]
                s2 = s[i:j]
                return all([s1[i]==s1[~i] for i in range(len(s1))]) or all(s2[i]==s2[~i] for i in range(len(s2)))
 
                
        return True
                