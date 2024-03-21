class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        count = 0
        for ch in s:
            if ch == "(":
                st.append(ch)
            else:
                if st:
                    st.pop()
                else:
                    count+=1
        return count+len(st)
            
        