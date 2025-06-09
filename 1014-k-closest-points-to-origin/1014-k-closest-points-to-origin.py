class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        for point in points : 
            distance = point[0] ** 2 + point[1] ** 2 
            heap.append([distance, point[0] , point[1]])
        
        heapq.heapify(heap)
        i = 0
        while i < k : 
            res.append(heapq.heappop(heap)[1:])
            i+=1 

        return res 
