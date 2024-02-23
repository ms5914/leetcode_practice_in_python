class Solution:
    
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        st = []
        st.append(-1)
        
        for i, ch in enumerate(s): 
            if ch == '(':
                st.append(i)
            if ch == ')':
                if st[-1] == -1 or s[st[-1]] == ')':
                    st.append(i)
                else:
                    st.pop()
                    max_len = max(max_len, i-st[-1])
                    print("max_len",max_len)
        return max_len
                    
                    
                    