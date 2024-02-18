class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
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
        
        
        while stack[-1] != -1:
            current_index = stack.pop()
            current_height = heights[current_index]
            width = len(heights)-stack[-1]-1
            max_area = max(max_area, width*current_height)
        return max_area
            
            
            
            
        