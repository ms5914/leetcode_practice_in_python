class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        
        #Solution 2 Do level-wise bfs from both directions
        if not wordList or not beginWord or not endWord or not endWord in wordList or beginWord == endWord:
            return 0
        
         
        #generic bfs for both directions. Simultaneously check if we have seen the same word in other bfs. If yes that means we have found a common word (level). Return a result
        def do_bfs(q, visited, other_visited):
            for i in range(len(q)):
                word = q.popleft()
                if word in other_visited:
                    return visited[word]+other_visited[word]-1 #-1 to avoid double counting the middle word

                
                for i in range(len(word)):
                    for neighbor in adj_list[word[:i]+'*'+word[i+1:]]:
                        if neighbor not in visited:
                            visited[neighbor] = visited[word]+1
                            q.append(neighbor)
            return 0
        
        

        #Making adjacency list using generic word. See solution 1
        adj_list = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                adj_list[word[:i]+'*'+word[i+1:]].append(word)
        
        front_queue = deque([beginWord])
        front_visited = {beginWord:1}
        
        rear_queue = deque([endWord])
        rear_visited = {endWord:1}
        
        even = True
        
        while front_queue and rear_queue: 
            #Traverse the shorter queue. You can do even odd as well. Like maintain a bool and if true traverse front_queue and make it false and vice versa. That will also work
            if len(front_queue) <= len(rear_queue):
                ans = do_bfs(front_queue, front_visited, rear_visited )
                if ans:
                    return ans
            else:
                ans = do_bfs(rear_queue, rear_visited, front_visited )
                if ans:
                    return ans
        return 0
                
                
# front deque(['hbo'])
# {'hbo': 1}
# rear deque(['qbx'])
# {'qbx': 1}


# front deque(['abo', 'hco', 'hbw'])
# {'hbo': 1, 'abo': 2, 'hco': 2, 'hbw': 2}
# rear deque(['qbx'])
# {'qbx': 1}


# front deque(['abo', 'hco', 'hbw'])
# {'hbo': 1, 'abo': 2, 'hco': 2, 'hbw': 2}
# rear deque(['qbq', 'qby', 'qbz', 'qbw'])
# {'qbx': 1, 'qbq': 2, 'qby': 2, 'qbz': 2, 'qbw': 2}


# front deque(['hco', 'hbw', 'ado', 'abq'])
# {'hbo': 1, 'abo': 2, 'hco': 2, 'hbw': 2, 'ado': 3, 'abq': 3}
# rear deque(['qbq', 'qby', 'qbz', 'qbw'])
# {'qbx': 1, 'qbq': 2, 'qby': 2, 'qbz': 2, 'qbw': 2}


# front deque(['hbw', 'ado', 'abq', 'hcd', 'hcj'])
# {'hbo': 1, 'abo': 2, 'hco': 2, 'hbw': 2, 'ado': 3, 'abq': 3, 'hcd': 3, 'hcj': 3}
# rear deque(['qbq', 'qby', 'qbz', 'qbw'])
# {'qbx': 1, 'qbq': 2, 'qby': 2, 'qbz': 2, 'qbw': 2}


# front deque(['hbw', 'ado', 'abq', 'hcd', 'hcj'])
# {'hbo': 1, 'abo': 2, 'hco': 2, 'hbw': 2, 'ado': 3, 'abq': 3, 'hcd': 3, 'hcj': 3}
# rear deque(['qby', 'qbz', 'qbw', 'abq'])
# {'qbx': 1, 'qbq': 2, 'qby': 2, 'qbz': 2, 'qbw': 2, 'abq': 3}


# front deque(['hbw', 'ado', 'abq', 'hcd', 'hcj'])
# {'hbo': 1, 'abo': 2, 'hco': 2, 'hbw': 2, 'ado': 3, 'abq': 3, 'hcd': 3, 'hcj': 3}
# rear deque(['qbz', 'qbw', 'abq'])
# {'qbx': 1, 'qbq': 2, 'qby': 2, 'qbz': 2, 'qbw': 2, 'abq': 3}


# front deque(['hbw', 'ado', 'abq', 'hcd', 'hcj'])
# {'hbo': 1, 'abo': 2, 'hco': 2, 'hbw': 2, 'ado': 3, 'abq': 3, 'hcd': 3, 'hcj': 3}
# rear deque(['qbw', 'abq'])
# {'qbx': 1, 'qbq': 2, 'qby': 2, 'qbz': 2, 'qbw': 2, 'abq': 3}


# front deque(['hbw', 'ado', 'abq', 'hcd', 'hcj'])
# {'hbo': 1, 'abo': 2, 'hco': 2, 'hbw': 2, 'ado': 3, 'abq': 3, 'hcd': 3, 'hcj': 3}
# rear deque(['abq', 'hbw'])
# {'qbx': 1, 'qbq': 2, 'qby': 2, 'qbz': 2, 'qbw': 2, 'abq': 3, 'hbw': 3}

# Output

                
        

                        
            
                
        
        
        
#         #Solution 1
#         reachable = defaultdict(list)
        
# # This was a bad approach, because for finding out neighbors we were double iterating the wordlist. See the double loop commented further down
# #         def is_reachable(word1, word2):
# #             if len(word1) != len(word2):
# #                 return False
            
# #             differ = False
# #             for i in range(len(word1)):
# #                 if word1[i]!=word2[i]: 
# #                     if differ:
# #                         return False
# #                     else:
# #                         differ = True
# #             return True
        
#         for word in wordList:
#             for j in range(len(word)):
                
#                 #Instead make generic key for every word. 
#                 reachable[word[:j]+"*"+word[j+1:]].append(word)
        
#             #Bad approach    
#             # for j in range(i+1, len(wordList)):
#             #     if is_reachable(wordList[i], wordList[j]):
#             #         reachable[wordList[i]].append(wordList[j])
#             #         reachable[wordList[j]].append(wordList[i])
                    
# #         for i in range(len(wordList)):
# #             if is_reachable(beginWord, wordList[i]):
# #                 reachable[wordList[i]].append(beginWord)
# #                 reachable[beginWord].append(wordList[i])
                
                
#         if beginWord == endWord or not beginWord or not wordList or not endWord or not endWord in wordList:
#             return 0
        
#         q = deque()
#         level = 0
#         visited = set()
#         q.append([beginWord, 1])
#         visited.add(beginWord)
        
#         while q:
#             word, count = q.popleft()
#             if word == endWord:
#                 return count
            
#             for i in range(len(word)):
#                 generic_key = word[:i]+"*"+word[i+1:]
#                 for word1 in reachable[generic_key]:
#                     if word1 not in visited:
#                         visited.add(word1)
#                         q.append([word1, count+1])
        
#         return 0
    
    
    
        
        
        
        
        
        
        
        
        
        
        
            
                
        