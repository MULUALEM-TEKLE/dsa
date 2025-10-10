from heapq import heappop , heappush
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = (10**9)+7

        adj = defaultdict(list)

        for src, dst, time in roads : 
            adj[src].append([dst , time])
            adj[dst].append([src , time])
        
        pq = [(0 , 0)]
        path_cost = [float('inf')] * n
        path_count = [0] * n
        path_count[0] = 1

        while pq : 
            t , node = heappop(pq)
            for neighbor , neighbor_cost in adj[node] : 
                new_cost = t + neighbor_cost
                if new_cost < path_cost[neighbor] : 
                    path_cost[neighbor] = new_cost
                    path_count[neighbor] = path_count[node]
                    heappush(pq , (new_cost , neighbor))
                elif new_cost == path_cost[neighbor] : 
                    path_count[neighbor] = (path_count[neighbor] + path_count[node]) % MOD

        return path_count[n-1]