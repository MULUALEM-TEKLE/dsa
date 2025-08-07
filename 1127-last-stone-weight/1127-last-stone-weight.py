class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [stone * -1 for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1 : 
            x , y = heapq.heappop(heap) , heapq.heappop(heap)
            if x != y :
                heapq.heappush(heap , -1*abs(x-y))
        
        if len(heap) > 0 : 
            return heap[0] * -1
        else : 
            return 0