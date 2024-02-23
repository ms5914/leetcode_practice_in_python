class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        i = 0
        while i<len(asteroids):
            if not st or st[-1]*asteroids[i]>0 or (st[-1]<0 and asteroids[i]>0):
                st.append( asteroids[i])
                i+=1
            else:
                if abs(st[-1])>abs(asteroids[i]):
                    i+=1
                elif abs(st[-1]) == abs(asteroids[i]):
                    st.pop()
                    i+=1
                else:
                    st.pop()
        return st
                
                
            
            
            
                        
        