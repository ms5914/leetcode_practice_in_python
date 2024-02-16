class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            top = self.min_stack[-1]
            self.min_stack.append(min(top, val))
            
    
    def pop(self) -> None:
        self.min_stack.pop()
        return self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        min_val = self.min_stack[-1]
        return min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()