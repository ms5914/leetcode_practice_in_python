class Solution:
    def calculate(self, s: str) -> int:
        def calculate_expr(s, start):
            operators = set(['+', '-'])
            number = 0
            sign = 1
            res = 0
            i = start
            while i < len(s):
                ch = s[i]
                if ch.isdigit():
                    
                    #Generate the number
                    number=number*10+int(ch)
                    i+=1
                    continue
                elif ch in operators:
                    
                    #Add the previous numbers sign and digits
                    res+=sign*number
                    
                    #Change sign for next number
                    sign = 1 if ch == '+' else -1
                    
                    #Reset number to zero so that it can hold a new number
                    number = 0
                    i+=1
                elif ch == '(':
                    
                    #Create new number and get end index of this expression inside bracket
                    number , ind = calculate_expr(s, i+1)
                    
                    #Set current index to this new index after the expression
                    i = ind+1
                
                elif ch == ')':
                    
                    #An expression has ended break and send results
                    break
                    
                elif ch == " ":
                    
                    #Do nothing
                    i+=1
                    continue
            
            
            #Generate final result, last number and its sign needs to be added
            res+=sign*number
            
            #return result of current expression and last index of this expression. Usually ')' or the len(s)
            return res, i
        
        return calculate_expr(s, 0)[0]

# class Solution:
#     def calculate(self, s: str) -> int:
        
#         def recurs(s, start):
#             operand = result = 0
#             nextSign = 1 # 1 for positive, -1 for negative (used to change sign of operand since we're always adding)
#             i = start
#             while i < len(s) - 1:
#                 i += 1
#                 c = s[i]
                
#                 if c == " ":
#                     continue

#                 if c.isdigit():
#                     # add digit to operand (could be multiple)
#                     operand = 10 * operand + int(c)
#                 elif c == "(":
#                     # new sub-expression - recurs
#                     end, operand = recurs(s, i)
#                     i = end
#                 elif c == ")":
#                     # sub-expression ended - exit
#                     break
#                 else:
#                     # operator
#                     result += nextSign * operand
#                     nextSign = 1 if c == "+" else -1
#                     operand = 0

#             return i, result + (nextSign * operand)
        
#         return recurs(s, -1)[1]
                    
                    
                    
                
                