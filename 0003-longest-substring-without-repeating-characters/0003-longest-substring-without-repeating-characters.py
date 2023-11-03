class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        i,j=0,0
        hm={}
        max_len=1
        while j<len(s):
            if s[j] in hm:
                while i<=hm[s[j]]:
                    i+=1
            hm[s[j]]=j
            max_len = max(max_len, j-i+1)
            j+=1
        return max_len

        