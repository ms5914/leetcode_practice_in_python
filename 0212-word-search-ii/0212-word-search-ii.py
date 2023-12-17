class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        
        
        if not board or not words:
            return []
         
        result = []
        
        class TrieNode:
            def __init__(self):
                self.word = False
                self.children = defaultdict(TrieNode)
            
            def print_words(self):
                if self.word:
                    print(word)
                for ch in self.children:
                    self.children[ch].print_words()

        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch in node.children:
                    node = node.children[ch]
                else:
                    newNode = TrieNode()
                    node.children[ch] = newNode
                    node = newNode
            node.word = word
        
        
            
        m = len(board)
        n = len(board[0])
        visited = set()


        def dfs(i,j, root):
            letter = board[i][j]
            node = root.children[letter]
            if node.word:
                result.append(node.word)
                node.word = False

            visited.add((i,j))
            delta = [(0, 1), (0, -1), (1,0), (-1, 0)]
            for k in range(len(delta)):
                new_i, new_j = i+delta[k][0], j+delta[k][1]
                if new_i>=0 and new_i<m and new_j>=0 and new_j<n and not (new_i, new_j) in visited and board[new_i][new_j] in node.children:
                    dfs(new_i, new_j, node)
            visited.remove((i,j))

            if not node.children:
                root.children.pop(letter)

        for i in range(m):
            for j in range(n):
                if board[i][j] in root.children:
                    dfs(i,j,root)

        return result
        
        
        
            
        