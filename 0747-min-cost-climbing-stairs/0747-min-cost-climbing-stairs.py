class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def climb(i) : 
            if i < 2 :
                return 0 
            return min(climb(i-1) + cost[i-1] , climb(i-2) + cost[i-2])
        return climb(len(cost))
