class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        s = s+")"
        num = 0
        sign = '+'
        stack = []
        result = 0
        while i<len(s):
            # print(stack)
            # print(num)
            # print(sign)
            if s[i].isdigit():
                while i<len(s) and s[i].isdigit():
                    num = num*10+int(s[i])
                    i+=1
            elif s[i] in ('+', '-', '*', '/', ')'):
                if sign in ('+', '-'):
                    new_sign = 1 if sign == '+' else -1
                    stack.append(new_sign*num)
                    num = 0
                    sign = s[i]
                    i+=1
                else:
                    num1 = stack.pop()
                    num2 = num
                    if sign == "*":
                        stack.append(num1*num2)
                    else:
                        stack.append(int(num1/num2))
                    sign = s[i]
                    i+=1
                    num = 0
            elif s[i] == " ":
                i+=1
        while stack:
            elem = stack.pop()
            result+=elem
        
        return result
            
            
            
            
            
        