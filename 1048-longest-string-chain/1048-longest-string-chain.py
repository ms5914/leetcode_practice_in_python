class Solution:
    
    def find_one_char_difference(self, word1, word2):
        if len(word1)==len(word2)-1:
            for i in range(len(word1)):
                if word1[i]==word2[i]:
                    continue
                else:
                    return word1[i:]==word2[i+1:]
            return True
        else:
            return False
        
    def longestStrChain(self, words: List[str]) -> int:
        if len(words)<=1:
            return len(words)
        
        words.sort(key=lambda v: len(v))
        
        #Create a map of key = len of word , val = (word, max_possible sequence with this word so far)
        mapp = defaultdict(list)
        mapp[len(words[0])].append((words[0],1))
        result = 1
        
        
        for index, value in enumerate(words[1:],1):
            curr_length, curr_word = len(value), value
            if curr_length-1 in mapp:
                maximum = 1
                possible_words = mapp[curr_length-1]
                for seq,length in possible_words:
                    if self.find_one_char_difference(seq, value):
                        maximum = max(maximum, length+1)
                result = max(result, maximum)   
                mapp[(curr_length)].append((value, maximum))
            else:
                mapp[(curr_length)].append((value, 1))
                
        return result
    
    #Lee's code very very efficient:
        # def longestStrChain(self, words):
        # dp = {}
        # for w in sorted(words, key=len):
        #     dp[w] = max(dp.get(w[:len(w)] + w[i + 1:], 0) + 1 )
        # return max(dp.values())
    
    
    