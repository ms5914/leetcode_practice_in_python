class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}
        
        
        if not s:
            return 0
        result=values[s[0]]
        i = 1
        
        while i < len(s):
            if values[s[i]] <= values[s[i-1]]:
                result+=values[s[i]]
                i+=1
            elif values[s[i]] > values[s[i-1]]:
                result-=values[s[i-1]]
                result+=(values[s[i]]-values[s[i-1]])
                i+=1
        
        return result
                
                
                
            
            
                
            
        
        