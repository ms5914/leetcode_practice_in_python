class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        #Since there can be any character in the string if we want to use a separator, we should escape it in the original string. 
        #Let's suppose we want to use '#' as a separator. We need to escape / and # characters by adding an extra / before them in the original string
        
        encoded_string = ""
        for word in strs: 
            encoded_string+=word.replace("/", "//").replace("#", "/#")+"#"
        return encoded_string


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        result = []
        word = ""
        while i<len(s):
            if s[i] == '/':
                word+=s[i+1]
                i+=2
            elif s[i] == '#':
                result.append(word)
                word=""
                i+=1
            else:
                word+=s[i]
                i+=1
        return result
            


        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))