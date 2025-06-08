class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [stone * -1 for stone in stones]
        heapq.heapify(heap)
        print(heap)
        while len(heap) > 1 : 
            x , y = heapq.heappop(heap) ,  heapq.heappop(heap)
            print(f"x = {x} , y = {y}")
            if x != y : 
                heapq.heappush(heap , abs(x-y) * -1)

        # return 1 
        res = heap[0] if len(heap) >= 1 else 0
        return abs(res)