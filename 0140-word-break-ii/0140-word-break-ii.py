class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        word_set = set(wordDict)
        result = []
        
        @lru_cache(maxsize=None)
        def find_sentences(i):
            if i == len(s):
                return [[]]
            result = []
            for k in range(i+1, len(s)+1):
                if s[i:k] in wordDict:
                    for sentence in find_sentences(k):
                        result.append([s[i:k]]+sentence)
            return result
        
        result_sentence = find_sentences(0)
        return [" ".join(li) for li in result_sentence ]

                    
            
                
        