class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list)

        for u,v,w in times : 
            adj[u].append((v , w))
        
        pq = [(0 , k)]
        times = {node : float('inf') for node in range(1,  n+1)}

        while pq : 
            w , node = heapq.heappop(pq)
            if w > times[node] : 
                continue

            times[node] = w  

            for neighbor , weight in adj[node] : 
                new_time = weight + w 
                if new_time < times[neighbor] : 
                    times[neighbor] = new_time 
                    heapq.heappush(pq , (new_time, neighbor))

        res = max(times.values())

        return res if res != float('inf') else -1
        
