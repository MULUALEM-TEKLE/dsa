class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        max_area = 0
        stack = [-1]

        for i in range(len(heights)) : 
            while stack[-1] != -1 and heights[stack[-1]] > heights[i] : 
                height = heights[stack.pop()]
                width = i - stack[-1] - 1 
                max_area = max(max_area , height * width)
            stack.append(i)
        
        return max_area
