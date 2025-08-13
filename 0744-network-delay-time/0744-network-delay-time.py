class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list)

        for u,v,w in times : 
            adj[u].append((v , w))
        
        pq = [(0 , k)]
        distance = {node:float('inf') for node in range(1 , n+1)}
        distance[k] = 0

        while pq : 
            w , node = heapq.heappop(pq)

            if w > distance[node] : 
                continue

            for neighbor , weight in adj[node] : 
                new_time = w + weight
                if new_time < distance[neighbor] :
                    distance[neighbor] = new_time 
                    heapq.heappush(pq , (new_time , neighbor))

        res = max(distance.values())

        return res if res != float('inf') else -1
        
