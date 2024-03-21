import re
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        
        start_end_pairs = []
        for word in words:
            start = s.find(word)
            while start!=-1:
                start_end_pairs.append([start,start+len(word)])
                start = s.find(word, start+1)
        
        if not start_end_pairs:
            return s
        start_end_pairs.sort(key = lambda x:x[0])
        
        unique_intervals = [[start_end_pairs[0][0],start_end_pairs[0][1]]]
        previous_end = start_end_pairs[0][1]
        
        for start, end in start_end_pairs[1:]:
            if start<=previous_end:
                previous_end = max(previous_end,end)
                unique_intervals[-1] = [unique_intervals[-1][0], previous_end]
            else:
                unique_intervals.append([start,end])
                previous_end = end
                
                
        result = [] 
        previous_end = 0
        
        for start,end in unique_intervals:
            result.append(s[previous_end:start])
            result.append('<b>')
            result.append(s[start:end])
            result.append('</b>')
            previous_end=end
        # Take the other remainder of the string
        result.append(s[previous_end:])
        return ''.join(result)
    
            
            
        
                
        
        
        
        # for word in words:
#             start_positions = [s.find_all(word)]
#             ending_positions = [x+len(word) for x in starting_positions]
        
#     sort:->
#         result = []
#         for index,ch in enumerate(s):
#             if ch in start_poisionts:
#                 running_bold_coutner+=1
#             if running_bold_counter==1:
#                 </bold.
        
#         ch in starting_positions:
#             counter=counter+1
#         if counter==1:
#             <bold>ch


#Easier Approach

# class Solution:
#     def addBoldTag(self, s: str, words: List[str]) -> str:
#         n = len(s)
#         bold = [False] * n
        
#         for word in words:
#             start = s.find(word)
#             while start != -1:
#                 for i in range(start, start + len(word)):
#                     bold[i] = True
                    
#                 start = s.find(word, start + 1)

#         open_tag = "<b>"
#         close_tag = "</b>"
#         ans = []
        
#         for i in range(n):
#             if bold[i] and (i == 0 or not bold[i - 1]):
#                 ans.append(open_tag)
                
#             ans.append(s[i])
            
#             if bold[i] and (i == n - 1 or not bold[i + 1]):
#                 ans.append(close_tag)
        
#         return "".join(ans)

        
        