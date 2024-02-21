class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        decr_stack = []
        result = [0 for i in range(len(temperatures))]
        
        for i,temp in enumerate(temperatures):
            while decr_stack and temperatures[decr_stack[-1]]<temp:
                popped_temp_index = decr_stack.pop()
                result[popped_temp_index] = i-popped_temp_index
            decr_stack.append(i)
        
        while decr_stack:
            popped_temp_index = decr_stack.pop()
            result[popped_temp_index] = 0
        
        return result
            
            
            
                
                
                
                
        
        
        