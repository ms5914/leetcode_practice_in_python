class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_water = 0
        stack = []
        for i, h in enumerate(height):
            if not stack or h <= height[stack[-1]]:
                stack.append(i)
            else:
                while stack and h > height[stack[-1]]:
                    left_small_index = stack.pop()
                    if not stack:
                        break
                    trapped_water+= (i-stack[-1]-1)*(min(height[stack[-1]], h)-height[left_small_index])
                stack.append(i)
        return trapped_water
        
            
            
            
                
            
        