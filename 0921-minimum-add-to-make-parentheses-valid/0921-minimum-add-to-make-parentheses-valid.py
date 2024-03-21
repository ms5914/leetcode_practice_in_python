class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        left_count = 0
        right_count = 0
        # for ch in s:
        #     if ch == "(":
        #         st.append(ch)
        #     else:
        #         if st:
        #             st.pop()
        #         else:
        #             count+=1
        # return count+len(st)
        for ch in s:
            if ch == "(":
                left_count+=1
            else:
                if left_count>0:
                    left_count-=1
                else:
                    right_count+=1
        return left_count+right_count
                
            
        