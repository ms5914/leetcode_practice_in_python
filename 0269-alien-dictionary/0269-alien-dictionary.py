class Solution:
    def alienOrder(self, words: List[str]) -> str:
        size = len(words)
        
        adjList = defaultdict(set)
        inEdges = defaultdict(int)
        
        inEdges = {c : 0 for word in words for c in word} #Remember to initialize this for all letters in a word in words. 
        
        
        #for every neighboring word, deduce dependencies. Find the first different letter at an index in every adjacent word, that will give us the dependency. 
        for i in range(size-1):
            j = 0
            while j<len(words[i]) and j<len(words[i+1]) and words[i][j] == words[i+1][j]:
                j+=1
            if j<len(words[i]) and j<len(words[i+1]):
                if not words[i+1][j] in adjList[words[i][j]]: 
                    #Updates adj list and inEdges only if for a particular dependency hasn't been counted before.This is important to remember. 
                    adjList[words[i][j]].add(words[i+1][j])
                    inEdges[words[i+1][j]]+=1
            
            elif len(words[i+1])<len(words[i]):
                return ""  
            #If the i+1 th word is a prefix of ith word, ordering is not possible. Remember this edge case.  
            
        #It's a DAG and now we are just doing topological sort using Kahn's algo to find the lexicographical order in Alien dictionary
        result = []
        q = deque([c for c in inEdges if inEdges[c]==0 ])
        while q:
            elem = q.popleft()
            result.append(elem)
            for letter in adjList[elem]:
                inEdges[letter]-=1
                if inEdges[letter] == 0:
                    q.append(letter)
        
        #We need to make sure that result has gotten all the letters otherwise there is a cycle. 
        return "".join(result) if len(result) == len(inEdges) else ""
            
            
        


        