class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        #Solution 2
        #This can also be done via recursion. The idea is to find the minimum lenght bar in between start and end. Now the max rectangle will be either the full rectangle made using this small bar from start to end. 
#This approach won't be optimized if the given heights array is sorted in either descending or ascending order. Because then we will not be making problems of n/2 or any fraction. It will be of the form T(n) = T(n-1)+cn which is O(n^2)
        
#         def find_max(start, end):
#             if start>end:
#                 return 0
#             else:
#                 min_height = float("inf")
#                 min_index = -1
#                 for i in range(start, end+1):
#                     if heights[i] <= min_height:
#                         min_height = heights[i]
#                         min_index = i
#                 return max(min_height*(end-start+1), find_max(start, min_index-1), find_max(min_index+1, end))
        
#         return find_max(0, len(heights)-1)
        



        
        
        
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
            
            
            
            
        