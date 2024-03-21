class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        mapp = defaultdict(list)
        
        #For each string, create a key such that it captures difference between each consectibe letter in the string. 
        #Then strings having the same key will belong to the same group. 
        for string in strings:
            curr = []
            for a,b in zip(string, string[1:]):
                remainder = (ord(b)-ord(a))%26
                curr.append(remainder)
            mapp[tuple(curr)].append(string)
        return list(mapp.values())
    
    
   