class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        if len(sentence1) != len(sentence2):
            return False
        
        parent = {}
        rank = {}
        
        for pair in similarPairs:
            for word in pair:
                if not word in parent:
                    parent[word] = word
                    rank[word] = 0
        
        
        def union(word1, word2):
            p1, p2 = find(word1), find(word2) #Union done using find method
            if p1==p2:
                return
            elif rank[p1]>rank[p2]:
                parent[p2] = p1
                rank[p1]+=1
            else:
                parent[p1] = p2
                rank[p2]+=1
        
        def find(word1):            #Finding the top most parent element 
            if parent[word1] == word1:
                return word1
            else:
                parent[word1] = find(parent[word1]) #By storing this, next time the number of hoops will decrease
                return parent[word1]
        
        
        for pair in similarPairs:
            union(pair[0], pair[1]) #Union those, i.e make connected components? 
            
        
        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i]:
                continue
            if sentence1[i] not in parent or sentence2[i] not in parent:
                return False
            if find(sentence1[i]) != find(sentence2[i]):
                return False
        return True
            
        
        
        
    
    
                    
                    
        
        
                    
            