class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {0:0 , 1:0}
        def climb(i) : 
            if i in memo : return memo[i]
            memo[i] = min(climb(i-1) + cost[i-1] , climb(i-2) + cost[i-2])
            return memo[i]
        return climb(len(cost))
