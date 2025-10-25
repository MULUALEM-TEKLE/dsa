class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = ceil(total/2)
        @cache
        def explore(i , cur) : 
            if cur >= target or i == len(stones) : 
                return abs(cur - (total - cur))
            return min(explore(i + 1 , cur + stones[i]) , explore(i + 1 , cur ))

        return explore(0 , 0)
     
