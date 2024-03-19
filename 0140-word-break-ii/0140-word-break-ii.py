class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        word_set = set(wordDict)
        result = []
        def find_sentences(i, sentence):
            if i == len(s):
                result.append(" ".join(sentence[:]))
            for k in range(i+1, len(s)+1):
                if s[i:k] in wordDict:
                    print(s[i:k])
                    sentence.append(s[i:k])
                    find_sentences(k, sentence)
                    sentence.pop()
        
        find_sentences(0,[])
        return result
        
                
                    
                    
            
                
        