class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        i = 0
        st = []
        #discard_index = set()
        while i<len(s):
            if s[i] == '(':
                st.append(i)
            elif s[i] == ')':
                if len(st)>0:
                    top = st[-1]
                    if s[top] == '(':
                        st.pop()
                    else:
                        st.append(i)
                else:
                    st.append(i)
            i+=1
            
        i, j = 0, 0
        result = []
        while i<len(s) and j<len(st):
            if i != st[j]:
                result.append(s[i])   
            else:
                j = j+1
            i=i+1
            
        while i<len(s):
            result.append(s[i])
            i+=1
        
        return "".join(result)
                
            
        
        # for elem in st:
        #     discard_index.add(elem)
        
#         result = []
        
#         for i in range(len(s)):
#             if i not in discard_index:
#                 result.append(s[i])
        
#         return "".join(result)
            
            
                        
                
            
        