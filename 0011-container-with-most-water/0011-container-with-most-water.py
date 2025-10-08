class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0 

        left , right = 0 , len(height)-1

        while left < right : 
            # calculate area
            area = min(height[left] , height[right]) * (right-left)
            # maximize my result
            res = max(res , area)
            # move smaller pointer
            if height[left] < height[right] : 
                left += 1 
            else : 
                right -= 1 
        
        return res