class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list)

        for u,v,w in times : 
            adj[u].append((v , w))
        
        pq = [(0 , k)]
        visited = set()
        t = 0 

        while pq : 
            w , node = heapq.heappop(pq)
            if node in visited : 
                continue

            visited.add(node)
            
            t = max(t , w)

            for neighbor , weight in adj[node] : 
                if neighbor not in visited : 
                    heapq.heappush(pq , (w + weight , neighbor))

        return t if len(visited) == n else -1
        
