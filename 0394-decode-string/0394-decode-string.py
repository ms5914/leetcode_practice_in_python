class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        result = []
        i = 0
        while i<len(s):
            if s[i].isdigit():
                num =0
                while i<len(s) and s[i].isdigit():
                    num = num*10+int(s[i])
                    i+=1
                st.append(num)
            elif s[i].isalpha():
                st.append(s[i])
                i+=1
            elif s[i] == '[':
                st.append('[')
                i+=1
            elif s[i] == ']':
                res = []
                while st and st[-1] != '[':
                    current_str = st.pop()
                    res.append(current_str)
                    new_res = "".join(res[::-1])
                st.pop()
                new_str = []
                for k in range(int(st.pop())):
                    new_str.append(new_res)
                st.append("".join(new_str))
                i+=1
        return "".join(st)
        
            
            
            
                    
                    
                
        
        
        