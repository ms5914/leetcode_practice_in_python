class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        hm = {')':'(', '}':'{', ']':'['}
        for ch in s:
            if ch in [')', '}', ']']:
                if not st or st[-1] !=hm[ch]:
                    return False
                else:
                    st.pop()
            else:
                st.append(ch)
        
        return len(st) == 0
        