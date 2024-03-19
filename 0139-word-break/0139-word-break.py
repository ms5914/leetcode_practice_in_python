class Solution:      
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        
        @lru_cache(maxsize=None)
        def helper(index):
            if index==len(s):
                return True

            for i in range(index+1, len(s)+1):
                if s[index:i] in wordDict:
                    if helper(i):
                        return True
            return False
        
        return helper(0)
            
