class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        st = []
        for i,height in enumerate(heights):
            if not st or heights[st[-1]]>height:
                st.append(i)
            else:
                while st and heights[st[-1]]<=height:
                    st.pop()
                st.append(i)
        return st
    
        #Better approach without stack, just go from reverse and keep a max_height to check if current building is blocked or not.
#         n = len(heights)
#         answer = []
#         max_height = -1
        
#         for current in reversed(range(n)):
#             # If there is no building higher (or equal) than the current one to its right,
#             # push it in the answer array.
#             if max_height < heights[current]:
#                 answer.append(current)
            
#                 # Update max building till now.
#                 max_height = heights[current]
        
#         answer.reverse()
#         return answer