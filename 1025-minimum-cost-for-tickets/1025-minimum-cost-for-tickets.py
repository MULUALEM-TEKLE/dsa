'''
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.
durations = [1 , 7 , 30] -> day the ticket bought inclusive 

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.
-> minizing total cost

 

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
'''
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        durations = [1 , 7 , 30]

        def find(next_day  ) : 
            for index,day in enumerate(days) : 
                if day >= next_day : return index
            return len(days)

        @cache
        def solve(day) : 
            if day >= len(days) : return 0
            mincost = float('inf')
            for index,cost in enumerate(costs) : 
                next_day = days[day] + durations[index] - 1

                next_day_index = find(next_day+1 )
                print(next_day_index)

                mincost = min(mincost , solve(next_day_index) + cost)

            return mincost
        
        return solve(0)