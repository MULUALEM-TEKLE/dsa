class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total//2
        self.res = float('inf')
        @cache
        def explore(i , cur) : 
            if cur >= target or i == len(stones) : 
                self.res = min(self.res , abs(cur - (total - cur)))
                return 
            explore(i + 1 , cur + stones[i]) 
            explore(i + 1 , cur )

        explore(0 , 0)
        return self.res
     
