class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        diff_count = [[0 for i in range(len(s))] for j in range(len(s))]
        next_row = [0 for i in range(len(s)) ]

        for i in range(n-2, -1, -1):
            curr_row = [0 for i in range(len(s))]
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    curr_row[j] = next_row[j-1]
                else:
                    curr_row[j] = 1+min(next_row[j], curr_row[j-1])
            next_row = curr_row
        
        return curr_row[len(s)-1] <=k
                    
                
        