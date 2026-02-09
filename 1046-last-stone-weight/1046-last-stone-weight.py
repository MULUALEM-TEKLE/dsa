class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [stone*-1 for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1 : 
            x , y = heapq.heappop(stones) , heapq.heappop(stones)
            if x != y : 
                heapq.heappush(stones, abs(x-y)*-1)
        
        if len(stones) : 
            return stones[0] * -1 
        
        return 0