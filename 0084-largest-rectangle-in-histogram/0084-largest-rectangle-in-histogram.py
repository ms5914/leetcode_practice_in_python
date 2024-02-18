class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        #The idea is that for every bar we need to find what is the max rectangle that we can make for that bar. Essentially we need to find the first bar that has height less than the current bar from both sides. This is the perfect case for stacks (Next smaller element). We will maintain a montonic increasing stack. As soon as we get a height that is less than the bar height present at the top of the stack, that means, we have gotten the next smaller element of that top bar and already we have previous small height bar on the left in the stack. 
        
        #We will be storing indexes instead of heights for ease of programming and calculating widths. 
        
        stack = []
        
        #We need to append this to calculate heights in case of first bar. Since it won't have a previous smaller bar. 
        stack.append(-1)
        max_area = -1*float("inf")
        for i,h in enumerate(heights):
            if not stack or heights[stack[-1]]<=h:
                stack.append(i)
            else:
                while stack[-1] != -1 and heights[stack[-1]]>h:
                    current_index = stack.pop()
                    current_height = heights[current_index]
                    width = i-stack[-1]-1
                    max_area = max(max_area, width*current_height)
                stack.append(i)
        
        
        #Now in the stack we will have montonically increasing bar heights. This means that these bars doesn't have a next smaller element on right. So the width will be now be len(heights)-stack[-1]-1 for each popped height. 
        while stack[-1] != -1:
            current_index = stack.pop()
            current_height = heights[current_index]
            width = len(heights)-stack[-1]-1
            max_area = max(max_area, width*current_height)
        return max_area
            
            
            
            
        