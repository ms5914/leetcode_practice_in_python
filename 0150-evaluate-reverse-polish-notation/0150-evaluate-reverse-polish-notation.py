class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        if not tokens:
            return 0
        calc_stack = []
                
        operators = {'+': lambda x,y:x+y, '-': lambda x,y:x-y, '*': lambda x,y: x*y, '/': lambda x,y:int(x/y)}
        
        for token in tokens:
            if token in operators:
                operand2, operand1 = calc_stack.pop(), calc_stack.pop()
                calc_stack.append(operators[token](operand1, operand2))
            else:
                calc_stack.append(int(token))
        
        return calc_stack.pop()
                
                
            
            
        
        
        