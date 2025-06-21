class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [[x**2 + y**2 , x , y] for x,y in points]
        heapq.heapify(heap)
        res = []
        for _ in range(k) : 
            r , x , y = heapq.heappop(heap)
            res.append([x , y])
        return res
