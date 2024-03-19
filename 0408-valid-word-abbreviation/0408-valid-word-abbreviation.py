class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        
        while i < len(word) and j < len(abbr):
            s = 0
            if abbr[j].isdigit():
                if int(abbr[j]) == 0:
                    return False
                while j< len(abbr) and abbr[j].isdigit():
                    s = s*10+int(abbr[j])
                    j+=1

                i+=s
                    
            elif i<len(word) and j<len(abbr) :
                if word[i] != abbr[j]:
                    return False
                i+=1
                j+=1
        return i == len(word) and j == len(abbr)
               
                
                
        
        