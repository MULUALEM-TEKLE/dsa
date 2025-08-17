class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points = [(p[0] , p[1]) for p in points]

        def distance(p1 , p2) : 
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        
        adj = defaultdict(list)

        for i in range(len(points)) : 
            for j in range(i+1 , len(points)) : 
                src , dst = i , j
                weight = distance(points[src] , points[dst])
                adj[src].append([dst , weight])
                adj[dst].append([src , weight])
        
        minheap = [(0 , 0)] # weight to it self (weight , dest)
        
        cost = 0
        visited = set()
       

        while minheap : 
            weight , dst = heapq.heappop(minheap)
            if dst in visited : continue
            cost += weight
            visited.add(dst)

            for neighbor , weight in adj[dst] : 
                if neighbor not in visited : 
                    heapq.heappush(minheap , [ weight , neighbor])

        return cost 