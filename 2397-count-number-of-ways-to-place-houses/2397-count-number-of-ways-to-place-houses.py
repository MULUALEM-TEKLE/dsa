'''
There is a street with n * 2 plots
where there are n plots on each side of the street.
    -> n on the left of the street 
    -> n on the right of the street 
The plots on each side are numbered from 1 to n. On each plot, a house can be placed.
    -> 1 indexed 
    -> 1 house per plot
Return the number of ways houses can be placed such that no two houses are adjacent to each other on the same side of the street. 
    -> count number of ways
    -> constraint -> no two houses can be next to each other on the same side 
    -> pick and skip?

Since the answer may be very large, return it modulo 109 + 7.
    -> output formating

Note that if a house is placed on the ith plot on one side of the street, a house can also be placed on the ith plot on the other side of the street
    -> no limit on having houses on the same plot across the street


Input: n = 1
Output: 4
Explanation: 
Possible arrangements:
1. All plots are empty. -> not picking???
2. A house is placed on one side of the street.
3. A house is placed on the other side of the street.
4. Two houses are placed, one on each side of the street.

lets focus on a single street
-> n plots 
-> can not have adjacent houses
-> on a plot I can choose to place a house or not 
    -> if I place a house I can not place a house next to it 

recurrence : 
    -> choose to take or skip
    -> if i place a house I can not place next to it
    -> if i skip I can just start from the next plot 
'''
class Solution:
    def countHousePlacements(self, n: int) -> int:
        memo = {0:1 , 1:2}
        def place(m) :
            if m in memo : return memo[m]
            memo[m] = place(m-1) + place (m-2)
            return memo[m]
        return (place(n) * place(n)) % ((10**9) + 7)