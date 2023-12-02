class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        reachable = defaultdict(list)
        
# This was a bad approach, because for finding out neighbors we were double iterating the wordlist. See the double loop commented further down
#         def is_reachable(word1, word2):
#             if len(word1) != len(word2):
#                 return False
            
#             differ = False
#             for i in range(len(word1)):
#                 if word1[i]!=word2[i]: 
#                     if differ:
#                         return False
#                     else:
#                         differ = True
#             return True
        
        for word in wordList:
            for j in range(len(word)):
                
                #Instead make generic key for every word. 
                reachable[word[:j]+"*"+word[j+1:]].append(word)
        
            #Bad approach    
            # for j in range(i+1, len(wordList)):
            #     if is_reachable(wordList[i], wordList[j]):
            #         reachable[wordList[i]].append(wordList[j])
            #         reachable[wordList[j]].append(wordList[i])
                    
#         for i in range(len(wordList)):
#             if is_reachable(beginWord, wordList[i]):
#                 reachable[wordList[i]].append(beginWord)
#                 reachable[beginWord].append(wordList[i])
                
                
        if beginWord == endWord or not beginWord or not wordList or not endWord or not endWord in wordList:
            return 0
        
        q = deque()
        level = 0
        visited = set()
        q.append([beginWord, 1])
        visited.add(beginWord)
        
        while q:
            word, count = q.popleft()
            if word == endWord:
                return count
            
            for i in range(len(word)):
                generic_key = word[:i]+"*"+word[i+1:]
                for word1 in reachable[generic_key]:
                    if word1 not in visited:
                        visited.add(word1)
                        q.append([word1, count+1])
        
        return 0
        
        
        
        
        
        
        
        
        
        
        
            
                
        