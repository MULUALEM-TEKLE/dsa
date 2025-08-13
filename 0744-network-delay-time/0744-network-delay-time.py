class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build adjacency list: node -> [(neighbor, weight)]
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        # Priority queue: (time, node), starting from node k at time 0
        pq = [(0, k)]
        visited = set()
        t = 0  # Tracks maximum time to reach any node
        
        while pq:
            w, node = heapq.heappop(pq)  # Get node with smallest current time
            if node in visited:
                continue
            visited.add(node)
            t = max(t, w)  # Update max time to reach any node
            
            # Explore neighbors
            for neighbor, weight in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (w + weight, neighbor))
        
        # Return max time if all nodes reached, else -1
        return t if len(visited) == n else -1