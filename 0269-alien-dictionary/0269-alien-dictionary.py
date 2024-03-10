class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        word_map = defaultdict(set)
        in_degree_count = defaultdict(int)
        char_set = {c for word in words for c in word }
        
            
        for word1, word2 in zip(words[:len(words)], words[1:]):
            i1, i2 = 0, 0
            while i1<len(word1) and i2<len(word2) and word1[i1] == word2[i2]:
                i1+=1
                i2+=1
                continue
                
                
            if i1<len(word1) and i2<len(word2):
                if not word2[i2] in word_map[word1[i1]]:
                    word_map[word1[i1]].add(word2[i2])
            elif len(word1)>len(word2):
                return ""
        
        for key, li in word_map.items():
            for val in li:
                in_degree_count[val]+=1
            
        q  = deque()
        for key in char_set:
            if in_degree_count[key] == 0:
                q.append(key)
        
        result = []
        while q:
            ch = q.popleft()
            result.append(ch)
            
            for nei in word_map[ch]:
                in_degree_count[nei]-=1
                if in_degree_count[nei] == 0:
                    q.append(nei)
        return "".join(result) if len(result) == len(char_set) else ""
                
            
                
                
                
            
                
                
            
                
            
        