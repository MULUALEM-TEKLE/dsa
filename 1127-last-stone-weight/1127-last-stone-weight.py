class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [stone * -1 for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1 : 
            x , y = heapq.heappop(heap) , heapq.heappop(heap)

            if x != y : 
                heapq.heappush(heap , abs(x - y) * -1 )
        
        if len(heap) : 
            return abs(heap[0])
        else : 
            return 0