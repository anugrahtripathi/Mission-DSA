def largestRectangleArea(heights: list[int]) -> int:
    max_area = 0
    stack = []  
    heights.append(0) 

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h_idx = stack.pop()
            h = heights[h_idx]
            if not stack:
                w = i
            else:
                w = i - stack[-1] - 1            
            max_area = max(max_area, h * w)        
        stack.append(i)  
    return max_area
