class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # minimizing total cost
        durations = [1 , 7 , 30]

        def find_nxt(start , dur) : 
            for i in range(start, len(days) ) : 
                if days[i] >= days[start]+dur : 
                    return i
            return len(days)
                
        @cache
        def explore(i) : 
            if i == len(days) : 
                return 0
        
            cost = float('inf')

            for j in range(len(costs)): 
                nxt_day = find_nxt(i , durations[j])
                cost = min(cost , costs[j]+explore(nxt_day))
            return cost
        
        return explore(0)

            
                