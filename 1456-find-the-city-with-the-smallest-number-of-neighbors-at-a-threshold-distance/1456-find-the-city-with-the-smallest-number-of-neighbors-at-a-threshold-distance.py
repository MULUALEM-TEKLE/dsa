class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)

        for src,dst,distance in edges : 
            adj[src].append([dst , distance])
            adj[dst].append([src , distance])
        
        def dijkstra(src) : 
            visited = set()
            minheap = [(0 , src)]

            while minheap : 
                distance , city = heapq.heappop(minheap)
                if city in visited : 
                    continue 
                
                visited.add(city)

                for neighbor,neighbor_distance in adj[city] : 
                    new_distance = distance+neighbor_distance
                    if new_distance <= distanceThreshold : 
                        heapq.heappush(minheap , [new_distance , neighbor])
            return len(visited)-1
        
        res , min_count = -1 , n
        for src in range(n) : 
            count = dijkstra(src)
            if count <= min_count : 
                res , min_count = src , count 
        
        return res