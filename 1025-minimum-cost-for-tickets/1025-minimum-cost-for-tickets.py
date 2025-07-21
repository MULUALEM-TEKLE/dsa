'''
You have planned some train traveling one year in advance. 
The days of the year in which you will travel are given as an integer array days. 
Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.

The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.
-> we are minimizing cost

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
-> buy only a single day pass
-> buy a 7 day pass, but now I have to check if the next day is beyond 7 days before anything
-> buy a 15 day pass, but now I have to check if the next day is beyond 15 days before anything
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
'''

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        ticket_durations = [1 , 7 , 30]
        @cache
        def buy(i ) :
            if i == len(days) : return 0
            minm = float('inf')
            for duration,cost in enumerate(costs) : 
                ticket_valid_until = days[i]+ticket_durations[duration]-1

                next_day_idx = bisect.bisect_left(days, ticket_valid_until + 1, lo=i)
              
                minm = min(minm , buy(next_day_idx) + cost) 
                # print(f"minm = {minm}")
            return minm
        return buy(0 )
