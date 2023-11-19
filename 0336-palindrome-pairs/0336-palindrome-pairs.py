class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        # #Hashmap approach
        # result = []
        # word_lookup = {word:i for i, word in enumerate(words)}

        # def find_valid_prefixes(word):
            
        #     valid_prefixes = []
        #     for i in range(len(word)):
        #         if word[i:] == word[i:][::-1]:
        #             valid_prefixes.append(word[:i])
        #     print("prefix",word,valid_prefixes)
        #     return valid_prefixes
        
        # def find_valid_suffixes(word):
        #     valid_suffixes = []
        #     for i in range(len(word)-1, -1, -1):
        #         if word[:i+1] == word[:i+1][::-1]:
        #             valid_suffixes.append(word[i+1:])
        #     print("suffix",word,valid_suffixes)
        #     return valid_suffixes

        
        # for i, word in enumerate(words):
        #     reversed_word = word[::-1]

        #     #Case 1 : The reverse is already present. Need to ignore the same index result if the word is already palindrome and appears as the reverse word. 
        #     if reversed_word in word_lookup and word_lookup[reversed_word] != i:
        #         result.append([i,word_lookup[reversed_word] ])
            
        #     #Case 2 : For all valid prefixes, find if their reverse exist. (This is first word)
        #     for prefix in find_valid_prefixes(word):
        #         reversed_prefix = prefix[::-1]
        #         if reversed_prefix in word_lookup:
        #             result.append([i, word_lookup[reversed_prefix]])
            
        #     #Case 3 : For all valid suffixes if their reverse exist (this is second word)
        #     for suffix in find_valid_suffixes(word):
        #         reversed_suffix = suffix[::-1]
        #         if reversed_suffix in word_lookup:
        #             result.append([word_lookup[reversed_suffix],i])

        # return result
        
        # #Trie approach

        class TrieNode:
            def __init__(self):
                self.children = collections.defaultdict(TrieNode)
                self.isEndIndex = -1
                self.validSuffixes = []
        
        root = TrieNode()
        for j,word in enumerate(words):
            current_node = root
            reversed_word = word[::-1]
            for i,c in enumerate(reversed_word):
                if reversed_word[i:] == reversed_word[i:][::-1]:
                    current_node.validSuffixes.append(j)
                current_node = current_node.children[c]
            current_node.isEndIndex = j
        
        solutions = []
        
        for j,word in enumerate(words):
            foundWord = True
            current_node = root
            for i, c in enumerate(word):
                if current_node.isEndIndex!=-1:
                    if word[i:] == word[i:][::-1]:
                        solutions.append([j,current_node.isEndIndex])
                
                if c not in current_node.children:
                    foundWord = False
                    break
                current_node = current_node.children[c]
                
            
            if foundWord: 
                if current_node.isEndIndex!=-1 and current_node.isEndIndex !=j :        
                    solutions.append([j,current_node.isEndIndex])
                for k in current_node.validSuffixes:
                    solutions.append([j,k])
        
        return solutions

            
            

            



            
        

            
















        
        
        

        




        