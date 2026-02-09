class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(x*x + y*y , [x , y]) for x , y in points]
        heapq.heapify(distances)
        res = []
        while k > 0 : 
            k -= 1
            res.append(heapq.heappop(distances)[1])
        return res 
