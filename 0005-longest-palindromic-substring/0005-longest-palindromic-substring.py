class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        max_len = 0
        max_str = ""
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True
            max_len = 1
            max_str = s[i:i+1]

        for i in range(n-1):
            j = i+1
            dp[i][j] = True if s[i]==s[j] else False
            if dp[i][j]:
                max_len = 2
                max_str = s[i:j+1]
        
        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i+k-1
                dp[i][j]=True if dp[i+1][j-1] and s[i]==s[j] else False
                if dp[i][j] and j-i+1>max_len:
                    max_len = j-i+1
                    max_str = s[i:j+1]
        
        return max_str
             


        

        