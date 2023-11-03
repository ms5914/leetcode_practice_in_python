class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
        counts = collections.Counter(s)
        if counts[s[0]] == len(s):
            return len(s)
        ans = 0
        for k in counts:
            ans+=(counts[k]//2)*2
        if ans < len(s):
            return ans+1
        return ans



        