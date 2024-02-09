class MyQueue:

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []
        

    def push(self, x: int) -> None:
        self.push_stack.append(x)
        

    def pop(self) -> int:
        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())
        val = self.pop_stack.pop()
        while self.pop_stack:
            self.push_stack.append(self.pop_stack.pop())
        return val
            
    def peek(self) -> int:
        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())
        
        val = self.pop_stack[-1]
        
        while self.pop_stack:
            self.push_stack.append(self.pop_stack.pop())
        
        return val
        
    
    def empty(self) -> bool:
        return len(self.push_stack) == 0
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()