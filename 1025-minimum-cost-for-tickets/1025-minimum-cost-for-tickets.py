class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        durations = [1 , 7 , 30]

        def find_next_day(next_valid_day) : 
            for index, day in enumerate(days) : 
                if day >= next_valid_day : return index
            return len(days)

        @cache
        def solve(i) : 
            if i >= len(days) : return 0

            min_cost = float('inf')

            for index , cost in enumerate(costs) : 
                next_valid_day = days[i] + durations[index] - 1

                next_valid_day_index = find_next_day(next_valid_day+1)

                min_cost = min(min_cost , cost + solve(next_valid_day_index))
            
            return min_cost
        
        return solve(0)