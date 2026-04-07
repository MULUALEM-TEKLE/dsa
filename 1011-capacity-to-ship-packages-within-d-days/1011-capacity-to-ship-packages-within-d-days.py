class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left , right = max(weights) , sum(weights)

        while left < right : 
            mid_capacity = (left+right)//2

            req_days = 1 
            current_load = 0 

            for w in weights : 
                if current_load + w > mid_capacity : 
                    current_load = 0 
                    req_days += 1 
                current_load += w 
            

            if req_days > days : 
                left = mid_capacity + 1 
            else : 
                right = mid_capacity 
        
        return left