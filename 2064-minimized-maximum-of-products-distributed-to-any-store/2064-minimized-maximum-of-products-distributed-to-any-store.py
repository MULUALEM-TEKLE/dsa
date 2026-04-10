class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        qts = quantities 
        low , high = 0 , max(qts)

        def can_do(amount) : 
            dist = 0 
            print(f"======{amount}======")
            for qt in qts : 
                # print(qt // amount )
                dist += math.ceil(qt / amount) 
            
            # print(f"for amount = {amount} we can distribute to {dist} stores")
            return dist <= n 

        
        res = high
        while low <= high : 
            mid_amount = (low+high)//2

            if mid_amount == 0 : 
                low = 1 
                continue 

            if can_do(mid_amount) : 
                res = mid_amount
                high = mid_amount - 1
            else : 
                low = mid_amount + 1
        
        return res 