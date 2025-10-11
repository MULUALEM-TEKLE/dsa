class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        area = 0

        for i, height in enumerate(heights) : 
            start = i
            while stack and height < stack[-1][0]   : 
                h , j = stack.pop()
                w = i-j
                area = max(area , h*w)
                start = j
            stack.append((height , start))
        

        while stack : 
            h , i = stack.pop()
            w = n-i
            area = max(area , h*w)
        

        return area