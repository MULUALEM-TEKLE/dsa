from heapq import heappop , heappush
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        points = [tuple(point) for point in points]

       
        for i in range(len(points)) : 
            x1 , y1 = points[i]
            for j in range(i+ 1 , len(points)) : 
                x2 , y2 = points[j]

                cost = abs(x1-x2) + abs(y1-y2)

                adj[(x1 , y1)].append([(x2 , y2) , cost])
                adj[(x2 , y2)].append([ (x1 , y1), cost])
        
        pq = []
        for neighbor, cost in adj[points[0]] : 
            heappush(pq , [cost , neighbor])

        total_cost = 0
        visited = set()
        visited.add(points[0])

        while pq : 
            cost , node = heappop(pq)
            if node in visited : 
                continue
            visited.add(node)
            total_cost += cost 
            for neighbor , cost in adj[node] : 
                if neighbor not in visited :
                    heappush(pq , [cost , neighbor])
        
        return total_cost