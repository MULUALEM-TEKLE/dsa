class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        durations = [1 , 7 , 30]
        def find(start , target_day) : 
            for i in range(start ,len(days)) :
                if days[i] >= target_day : 
                    return i
            return len(days) 
        @cache
        def solve(i) : 
            if i == len(days) : return 0 

            minm = float('inf')

            for duration,cost in enumerate(costs) : 
                ticket_duration = days[i]+durations[duration]-1

                next_index = find(i , ticket_duration+1)

                minm =min(minm,  cost + solve(next_index))
            return minm
        return solve(0)