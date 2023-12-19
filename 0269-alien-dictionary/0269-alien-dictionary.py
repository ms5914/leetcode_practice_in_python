class Solution:
    def alienOrder(self, words: List[str]) -> str:
        size = len(words)
        
        adjList = defaultdict(set)
        inEdges = defaultdict(int)
        
        inEdges = {c : 0 for word in words for c in word}
        
        for i in range(size-1):
            j = 0
            while j<len(words[i]) and j<len(words[i+1]) and words[i][j] == words[i+1][j]:
                j+=1
            if j<len(words[i]) and j<len(words[i+1]):
                if not words[i+1][j] in adjList[words[i][j]]:
                    adjList[words[i][j]].add(words[i+1][j])
                    inEdges[words[i+1][j]]+=1
            
            elif len(words[i+1])<len(words[i]):
                return ""
            
        
        
        result = []
        q = deque([c for c in inEdges if inEdges[c]==0 ])
        while q:
            elem = q.popleft()
            result.append(elem)
            for letter in adjList[elem]:
                inEdges[letter]-=1
                if inEdges[letter] == 0:
                    q.append(letter)
        
        return "".join(result) if len(result) == len(inEdges) else ""
            
            
        


        