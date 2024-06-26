# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        for element in nestedList[::-1]:
            self.stack.append(element)
            
        self.result = None
        while self.result==None and self.stack:
            self.result = self.stack.pop()
            if self.result.isInteger()==False:
                for elem in self.result.getList()[::-1]:
                    self.stack.append(elem)
                self.result = None
        print(self.stack, self.result)
    def next(self) -> int:
        previous = self.result
        
        self.result = None
        while self.result==None and self.stack:
            self.result = self.stack.pop()
            if self.result.isInteger()==False:
                for elem in self.result.getList()[::-1]:
                    self.stack.append(elem)
                self.result = None
        return previous
        
    
    def hasNext(self) -> bool:
        return self.result
    
    #Concise code
    
#     class NestedIterator:
    
#     def __init__(self, nestedList: [NestedInteger]):
#         self.stack = list(reversed(nestedList))
        
        
#     def next(self) -> int:
#         self.make_stack_top_an_integer()
#         return self.stack.pop().getInteger()
    
        
#     def hasNext(self) -> bool:
#         self.make_stack_top_an_integer()
#         return len(self.stack) > 0
        
        
#     def make_stack_top_an_integer(self):
#         # While the stack contains a nested list at the top...
#         while self.stack and not self.stack[-1].isInteger():
#             # Unpack the list at the top by putting its items onto
#             # the stack in reverse order.
#             self.stack.extend(reversed(self.stack.pop().getList()))
        
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())