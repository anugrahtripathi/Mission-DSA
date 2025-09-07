from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        stack = []
        total_water_trapped = 0
        i = 0
        while i < len(height):
            while stack and height[i] > height[stack[-1]]:
                popped_index = stack.pop()
                if not stack:
                    break                                
                distance = i - stack[-1] - 1
                water_height = min(height[i], height[stack[-1]]) - height[popped_index]                
                total_water_trapped += distance * water_height            
            stack.append(i)
            i += 1            
        return total_water_trapped
