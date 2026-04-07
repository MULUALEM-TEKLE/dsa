class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        def process_packages(capacity) : 
            days_ = 1
            current_load = 0 
            for w in weights :
                if current_load + w > capacity :
                    days_ += 1 
                    current_load = 0 
                current_load += w

            # print("=============")
            return days_
        
        low, high = max(weights) , sum(weights)
        res = sum(weights)
        # print(process_packages(27))

        while low < high : 
            mid = (low+high)//2
            if process_packages(mid) <= days :
                res = mid
                high = mid 
            else : 
                low = mid + 1

        return res  