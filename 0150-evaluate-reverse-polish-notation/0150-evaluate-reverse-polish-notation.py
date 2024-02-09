class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        if not tokens:
            return 0
        
        calc_stack = []
        
        def division(x,y):
           # print(f"HERE I AM{x},{y}")

            if (x>=0) ^ (y>=0):
                if abs(x)%abs(y) == 0:
                    return x//y
                else:
                    return (x//y)+1
           # print(f"HERE I AM{x},{y}")
            return x//y
                
                
            
        
        
        
        operators = {'+': lambda x,y:x+y, '-': lambda x,y:x-y, '*': lambda x,y: x*y, '/': lambda x,y:division(x,y)}
        
        for token in tokens:
           # print(calc_stack)
            if token in operators:
                operand2, operand1 = calc_stack.pop(), calc_stack.pop()
                calc_stack.append(operators[token](operand1, operand2))
            else:
                calc_stack.append(int(token))
        
        return calc_stack.pop()
                
                
            
            
        
        
        