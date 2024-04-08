class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        
        for word in strings:
            prev = word[0]
            key = ["1"]
            for ch in word[1:]:
                curr = ch
                key.append(str((ord(curr)-ord(prev))%26))
                prev = curr
            #print(key)
            hm[tuple(key)].append(word)
        
        return hm.values()
            
            
                
        