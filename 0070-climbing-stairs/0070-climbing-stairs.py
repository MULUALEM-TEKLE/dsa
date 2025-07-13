'''
You are climbing a staircase. 
It takes n steps to reach the top.
    -> height of the staircase is n

Each time you can either climb 1 or 2 steps.
    -> either increment or decrement 1 or 2 steps 
    -> decrement or increment from n

In how many distinct ways can you climb to the top?
    -> counting 
    -> combinatorics
    -> distinct == unique

Sample 
n = 2
1. 1 step + 1 step
2. 2 steps
res = 2

Base cases
    -> from step 0 there is 1 way to reach the 0th step
    -> from step 1 there is 1 way to reach the 0th step
    -> from step 2  there area 2 ways to reach the 0th step
            -> 2 -> 1 -> 0 
            -> 2 -> 0
how many ways to reach step 0 from step n
    -> ways it take to reach step n-1 and step n-2
    -> why?
-> n can not be less than 0
'''



class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def climb(n) : 
            if n == 1 : return 1
            if n == 2 : return 2
            return climb(n-2) + climb(n-1)
        
        return climb(n)
         