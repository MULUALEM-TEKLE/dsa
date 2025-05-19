import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        squared_list = [(point[0] ** 2  + point[1] ** 2) for point in points]
        table = {}
        for index , square in enumerate(squared_list) : 
            if square in table.keys() : 
                table[square].append(points[index])
            else :
                table[square] = [points[index]]

        heapq.heapify(squared_list)
        min = set(heapq.nsmallest(k , squared_list))
        res = []
        for m in min : 
            res.extend(table[m])

        return res